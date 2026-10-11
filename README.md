<!--
GitHub Profile README
Repository: jys96/jys96 (Special Repo - Profile)
Last updated: 2026-05-10
-->

<div align="center">

  <img src="https://capsule-render.vercel.app/api?type=waving&height=220&color=0:bdbcf6,100:fcdbe4&text=WELCOME&reversal=true&textBg=false&fontColor=FFFFFF&fontSize=50&fontAlignY=35&animation=fadeIn&stroke=8f64af70&strokeWidth=2&desc=상상을%20AI%20서비스로%20완성하는%20개발자,%20정유선입니다.&descAlignY=55" alt="header" />

</div>

<br />

## About Me

- **화면·API·데이터·AI를 하나의 서비스 흐름으로 연결하는 AI 풀스택 개발자입니다.**
- 퍼블리싱 · 프론트 · 풀스택 **4년 5개월 실무** → SKN AI 부트캠프 SKN23기 수료 (2026-05-20)
- 관심 영역: **RAG 설계 · LLM 응답 평가 · 벡터 검색 · 서비스 흐름 안정성**
<!--
- 진행 프로젝트: `withDOG` (반려견 동반 장소 추천)
-->

<br />

## Core Keywords

<div align="center">

  `AI Service Engineering` · `RAG Pipeline Design` · `LLM Evaluation`
    
  `AI UX Flow` · `FastAPI Backend` · `React Frontend` · `Docker / AWS Deployment`

</div>

<br />

## Featured Projects

### [withDOG](https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN23-FINAL-3TEAM) — Pet-friendly Place AI Service

반려견 동반 가능 장소를 추천하는 AI 챗봇

- **역할**: 3인 팀 / PM 겸 풀스택 — KoELECTRA 의도분류 fine-tuning · 시설정보 RAG 직접 구현
- **AI**: KoELECTRA · ko-sroberta · ChromaDB · OpenAI API
- **Stack**: React · FastAPI · Docker · AWS EC2 S3 RDS (MySQL)
- **결과**: KoELECTRA 의도분류 학습부터 FastAPI 서빙까지 단독 구현 (검증 정확도 0.9955), Hit@5 · Recall@5 · Refusal Rate 지표 계산과 회귀 실행 코드 작성, SK네트웍스 Family AI 캠프 23기 최종 프로젝트 우수상

### [On You](https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN23-4th-3Team) — AI Skincare Chatbot

얼굴 피부 이미지와 사용자 대화 기반 맞춤형 스킨케어 추천 챗봇

- **역할**: 5인 팀 / React 프론트엔드 · FastAPI 백엔드 · RAG 데이터 파이프라인 구현 (이미지 분석과 LangGraph 라우팅은 팀원 담당)
- **AI**: PubMed · 식약처 화장품 보고서 수집 · 번역 · 분할 후 ko-sroberta 임베딩으로 ChromaDB에 23만+ 조각 적재, RAG 검색 응답 연결
- **Stack**: React · Flutter · FastAPI · Docker · AWS EC2 S3 RDS (MariaDB)
- **결과**: 요청 → 분석 → 검색 → 응답 흐름을 단일 서비스로 통합, Google Play Store 내부 테스트까지 진행

### G-SAM — Media Asset Management Platform

방송사용 미디어 자산 관리 플랫폼 (제머나이소프트 재직 중 참여)

- **역할**: Frontend Lead / 풀스택 — Vue.js · PHP/Laravel
- **결과**: 플랫폼마다 달라 값이 틀어지던 SNS 통계 수집을 3단계 동기화 구조로 재설계, 핵심 기능인 SAM/Social 서비스를 CJ ENM · SBS · 아리랑TV에 도입, 솔루션 판매 및 유지보수 계약 확보를 통한 회사 매출 43% 이상 증가 기여

<br />

## Tech Stack

<div align="center">

### Main Stack

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=fff" />
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=fff" />
  <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=000" />
  <img src="https://img.shields.io/badge/Vue.js-4FC08D?style=for-the-badge&logo=vuedotjs&logoColor=fff" />
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=fff" />
  <img src="https://img.shields.io/badge/Flutter-02569B?style=for-the-badge&logo=flutter&logoColor=fff" />
</p>
<p>
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=fff" />
  <img src="https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazonaws&logoColor=fff" />
  <img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=000" />
  <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=fff" />
</p>

</div>

<details>
  <summary><b>전체 기술 스택 보기</b></summary>

<div align="center">

#### AI / LLM

<p>
  <img src="https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=fff" />
  <img src="https://img.shields.io/badge/Hugging%20Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=000" />
  <img src="https://img.shields.io/badge/LangGraph-1C3C3C?style=for-the-badge&logo=langchain&logoColor=fff" />
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=fff" />
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=fff" />
  <img src="https://img.shields.io/badge/LightGBM-3C8DBC?style=for-the-badge&logoColor=fff" />
  <img src="https://img.shields.io/badge/XGBoost-DC382D?style=for-the-badge&logoColor=fff" />
  <img src="https://img.shields.io/badge/ChromaDB-FF6F00?style=for-the-badge&logoColor=fff" />
  <img src="https://img.shields.io/badge/sentence--transformers-009688?style=for-the-badge&logoColor=fff" />
</p>

#### Backend

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=fff" />
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=fff" />
  <img src="https://img.shields.io/badge/PHP-777BB4?style=for-the-badge&logo=php&logoColor=fff" />
  <img src="https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=fff" />
</p>

#### Frontend

<p>
  <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=000" />
  <img src="https://img.shields.io/badge/Vue.js-4FC08D?style=for-the-badge&logo=vuedotjs&logoColor=fff" />
  <img src="https://img.shields.io/badge/Flutter-02569B?style=for-the-badge&logo=flutter&logoColor=fff" />
  <img src="https://img.shields.io/badge/Dart-0175C2?style=for-the-badge&logo=dart&logoColor=fff" />
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=fff" />
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=000" />
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=fff" />
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=fff" />
  <img src="https://img.shields.io/badge/Sass-CC6699?style=for-the-badge&logo=sass&logoColor=fff" />
  <img src="https://img.shields.io/badge/styled--components-DB7093?style=for-the-badge&logo=styledcomponents&logoColor=fff" />
</p>

#### Database

<p>
  <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=fff" />
  <img src="https://img.shields.io/badge/MariaDB-003545?style=for-the-badge&logo=mariadb&logoColor=fff" />
  <img src="https://img.shields.io/badge/ChromaDB-FF6F00?style=for-the-badge&logoColor=fff" />
</p>

#### Infra & DevOps

<p>
  <img src="https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazonaws&logoColor=fff" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=fff" />
  <img src="https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=fff" />
  <img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=000" />
</p>

#### Collaboration & Tools

<p>
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=fff" />
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=fff" />
  <img src="https://img.shields.io/badge/GitLab-FC6D26?style=for-the-badge&logo=gitlab&logoColor=fff" />
  <img src="https://img.shields.io/badge/Jira-0052CC?style=for-the-badge&logo=jira&logoColor=fff" />
  <img src="https://img.shields.io/badge/Redmine-B32024?style=for-the-badge&logo=redmine&logoColor=fff" />
  <img src="https://img.shields.io/badge/Notion-000?style=for-the-badge&logo=notion&logoColor=fff" />
  <img src="https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=slack&logoColor=fff" />
  <img src="https://img.shields.io/badge/Figma-F24E1E?style=for-the-badge&logo=figma&logoColor=fff" />
  <img src="https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=fff" />
</p>

</div>

</details>

<br />

## Currently Focusing On

- **RAG Evaluation** — Hit@5 · Recall@5 · Refusal Rate 지표 계산과 회귀 실행 자동화
- **AI Service Architecture** — 요청 → 분석 → 검색 → 응답 흐름 단일 서비스 설계
- **LLM Application Engineering** — 의도분류 경량 모델로 매 요청 LLM 호출을 줄이는 응답 흐름 설계
- **FastAPI 기반 AI Backend** — 비동기 처리 · 에러 핸들링 · 평가 자동화
- **AI UX / Service Flow** — AI 기능을 사용자 경험으로 완성하는 설계

<br />

## Engineering Workflow

> Obsidian + LLM 기반 개발 생산성 시스템. 코드·결정·트러블슈팅을 AI 가 읽고 캐시하는 워크플로우 운영.

- **Personal LLM Wiki** — 프로젝트 이슈·설계·결정·트러블슈팅 기록을 Obsidian + Claude 로 자동 캐시
- **Code Analysis Cache** — 같은 코드를 두 번 분석하지 않는 토큰 절약 흐름 (`wiki/{NN-카테고리}/` 9종)
- **Multi-AI Cross-Review** — Claude · GPT · Gemini · Codex 교차 검토로 산출물 정확도 강화
- **RAG · FastAPI · Infra 문제 해결 기록 아카이빙** — 동일 문제 재발생 시 즉시 회수 가능

<details>
  <summary><b>Wiki Stats (자동 갱신)</b></summary>

<!-- WIKI_STATS_BEGIN -->
- **총 문서**: 146+
- **이번 주 업데이트**: 146건
- **주요 카테고리**: _(태그 추출 대기 중)_
<!-- WIKI_STATS_END -->

</details>

<br />

## GitHub Stats

<div align="center">

  <img src="https://komarev.com/ghpvc/?username=jys96&label=Profile+Views&color=8f64af&style=flat" alt="Profile Views" />

  <br />

  <img src="https://raw.githubusercontent.com/jys96/jys96/main/github-metrics.svg" alt="GitHub Metrics" />

</div>

<br />

## Contact

<div align="center">

  <p>
    <img src="https://cdn.simpleicons.org/kakaotalk/FFCD00" width="20" valign="middle" alt="Kakao" />
    &nbsp;<a href="mailto:acft9609@kakao.com">acft9609@kakao.com</a>
  </p>
  <p>
    <img src="https://cdn.simpleicons.org/gmail/EA4335" width="20" valign="middle" alt="Gmail" />
    &nbsp;<a href="mailto:acft9609@gmail.com">acft9609@gmail.com</a>
  </p>

</div>

<br />

<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&height=120&color=0:fcdbe4,100:bdbcf6&section=footer" alt="footer" />
</div>
