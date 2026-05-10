#!/usr/bin/env python3
"""
Wiki stats extractor for jys96/jys96 GitHub profile README.

Behavior:
- wiki-self  : 총 문서 카운트 + 이번 주 업데이트만 추출 (민감 정보 보호)
- wiki-withDOG : 카운트 + 태그 빈도 추출 (sensitivity: high/medium 페이지는 태그 추출 스킵)
- README.md 의 <!-- WIKI_STATS_BEGIN --> ~ END 마커 사이만 갱신
"""
from __future__ import annotations

import datetime
import re
from collections import Counter
from pathlib import Path

import yaml

WIKI_ROOT = Path("_wiki")
README = Path("README.md")

# wiki-self 카테고리·민감 태그 블랙리스트 (방어용 — 기본적으로 wiki-self 태그는 추출 안 함)
TAG_BLACKLIST = {
    "self", "사람", "경험", "생각", "활동", "회고",
    "가족", "건강", "관계", "self/overview",
}

# 우선 노출하고 싶은 기술 태그 (있으면 top N에 우선 편입)
TAG_WHITELIST_PRIORITY = {
    "RAG", "LLM", "FastAPI", "ChromaDB", "LangGraph", "OpenAI",
    "Architecture", "Decision", "AI", "Backend", "Frontend",
    "Docker", "AWS", "Python", "Mentor", "API", "DB",
}

NOW = datetime.datetime.now(datetime.timezone.utc)
WEEK_AGO = NOW - datetime.timedelta(days=7)


def parse_frontmatter(content: str) -> dict | None:
    if not content.startswith("---"):
        return None
    parts = content.split("---", 2)
    if len(parts) < 3:
        return None
    try:
        return yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        return None


def collect(wiki_dir: Path, *, extract_tags: bool) -> dict:
    total = 0
    week = 0
    tags: Counter[str] = Counter()

    if not wiki_dir.exists():
        return {"total": 0, "week": 0, "tags": tags}

    for md in wiki_dir.rglob("*.md"):
        if not md.is_file():
            continue
        rel = md.relative_to(wiki_dir)
        # raw 자료, .obsidian, .git 제외
        if rel.parts and rel.parts[0] in {"raw", ".obsidian", ".git", "node_modules"}:
            continue
        # 인덱스/로그 제외 (선택)
        if rel.name.lower() in {"index.md", "log.md", "memory.md", "claude.md"}:
            continue

        total += 1

        mtime = datetime.datetime.fromtimestamp(md.stat().st_mtime, tz=datetime.timezone.utc)
        if mtime > WEEK_AGO:
            week += 1

        if not extract_tags:
            continue

        try:
            content = md.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue

        fm = parse_frontmatter(content)
        if not fm:
            continue

        # 민감 페이지 태그 추출 스킵
        if str(fm.get("sensitivity", "")).lower() in {"high", "medium"}:
            continue

        raw_tags = fm.get("tags") or []
        if isinstance(raw_tags, str):
            raw_tags = [raw_tags]
        for t in raw_tags:
            if not isinstance(t, str):
                continue
            t = t.strip()
            # `부트캠프/프로젝트/완료` 같은 슬래시 표기는 첫 토큰만
            t = t.split("/")[0].strip()
            if not t or t in TAG_BLACKLIST:
                continue
            tags[t] += 1

    return {"total": total, "week": week, "tags": tags}


def top_tags(counter: Counter[str], n: int = 6) -> list[str]:
    if not counter:
        return []
    priority = sorted(
        (t for t in counter if t in TAG_WHITELIST_PRIORITY),
        key=lambda t: -counter[t],
    )
    rest = [t for t, _ in counter.most_common() if t not in TAG_WHITELIST_PRIORITY]
    return (priority + rest)[:n]


def render_block(total: int, week: int, tags: list[str]) -> str:
    tags_md = " · ".join(f"`{t}`" for t in tags) if tags else "_(태그 추출 대기 중)_"
    return (
        "<!-- WIKI_STATS_BEGIN -->\n"
        f"- **총 문서**: {total}+\n"
        f"- **이번 주 업데이트**: {week}건\n"
        f"- **주요 카테고리**: {tags_md}\n"
        "<!-- WIKI_STATS_END -->"
    )


def main() -> None:
    self_stats = collect(WIKI_ROOT / "wiki-self", extract_tags=False)
    proj_stats = collect(WIKI_ROOT / "wiki-withDOG", extract_tags=True)

    total = self_stats["total"] + proj_stats["total"]
    week = self_stats["week"] + proj_stats["week"]
    tags = top_tags(proj_stats["tags"], n=6)

    new_block = render_block(total, week, tags)
    print(new_block)

    readme = README.read_text(encoding="utf-8")
    pattern = re.compile(
        r"<!-- WIKI_STATS_BEGIN -->.*?<!-- WIKI_STATS_END -->",
        re.DOTALL,
    )
    if pattern.search(readme):
        readme = pattern.sub(new_block, readme)
    else:
        # 마커가 README 에 없을 경우 끝에 부착 (안전 장치)
        readme = readme.rstrip() + "\n\n## Personal LLM Wiki\n\n" + new_block + "\n"

    README.write_text(readme, encoding="utf-8")


if __name__ == "__main__":
    main()
