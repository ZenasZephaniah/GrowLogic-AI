# GrowLogic AI


🌱 GrowLogic AI
Agentic AI-powered agricultural advisor for farmers, vendors, and policymakers


🚜 Problem Statement

Farmers in India face fragmented, unreliable access to agricultural information — from unpredictable weather to soil health, crop choices, pest threats, credit availability, and market fluctuations. Decision-making often relies on guesswork, leading to crop losses, debt cycles, and financial vulnerability. Current digital tools are siloed, lack explainability, and are often inaccessible in local languages or low-connectivity environments.

💡 Solution Overview

GrowLogic AI is an agentic AI-powered advisor designed to empower farmers and stakeholders with real-time, multilingual, explainable insights.
The system integrates weather forecasts, soil health data, crop science, financial schemes, and market prices into a single intelligent platform. Queries in natural language (including regional dialects) are processed via a retrieval-augmented generation (RAG) pipeline, ensuring fact-grounded and transparent responses.

Farmers can ask:
	•	“When should I irrigate?”
	•	“Which seed variety suits this soil and season?”
	•	“What subsidies can I access for irrigation?”
	•	“Should I sell my harvest now or wait for market improvement?”


✨ Key Features
	•	Multilingual Voice + Text Queries (supports code-switching and dialects).
	•	RAG-based AI Pipeline → grounded in agricultural datasets, minimizing hallucination.
	•	Explainable AI Outputs with citations & dataset references.
	•	Offline-first Support for low-connectivity areas.
	•	Cross-Domain Intelligence → weather, soil, crop, finance, market.



🏗️ Architecture
Layers:
	1.	User Interaction Layer → voice/text, multilingual support.
	2.	Processing Layer → language detection, intent classification.
	3.	Knowledge Retrieval → FAISS vector DB + weather APIs + soil/crop datasets.
	4.	Reasoning & Generation → RAG pipeline with Hugging Face LLMs.
	5.	Delivery Layer → FastAPI endpoints + mobile-ready frontend (PWA).


📊 Public Datasets Referenced
	•	IMD Weather Data – weather forecasts & rainfall patterns.
	•	Agmarknet – mandi crop prices.
	•	SoilGrids – global soil property maps.
	•	ICAR & KVK Publications – crop/pest advisories.
	•	Government Schemes – PM-Kisan, NABARD, crop insurance docs.


⚙️ Tech Stack
	•	Backend: Python, FastAPI, PostgreSQL, FAISS.
	•	ML/AI: Hugging Face Transformers, LangChain, RAG pipeline.
	•	Frontend: React/Next.js (PWA).
	•	Hosting (future scope): AWS S3/Lambda or GCP Functions.
	•	Visualization: Plotly/Matplotlib for trends.

## 🚀 Setup (Prototype Placeholder)
```bash
git clone https://github.com/ZenasZephaniah/GrowLogic-AI.git
cd GrowLogic-AI
# (Future) Setup instructions:
# python -m venv venv
# pip install -r requirements.txt
# uvicorn src.main:app --reload
```

## 📌 Current Status
- Documentation, datasets, and architecture included.
- Core RAG pipeline stubs in progress.
- Full prototype under active build, to be released post-hackathon.


## 🏆 Hackathon Submission Info
- Theme: The Challenge: Agentic AI in Agriculture
- Team: Groot
- Hackathon: Capital One Launchpad 2025

