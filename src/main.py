from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="GrowLogic-AI (prototype)")

class AskRequest(BaseModel):
    query: str
    top_k: Optional[int] = 5

class RetrieveRequest(BaseModel):
    doc_id: str

@app.post("/ask")
async def ask(req: AskRequest):
    """
    Prototype endpoint:
    - would: embed query, search FAISS, assemble context, call LLM.
    - For now: returns a placeholder structure showing pipeline steps.
    """
    # placeholder response showing the intended flow
    return {
        "query": req.query,
        "pipeline": [
            "embed(query)",
            "faiss.search(top_k)",
            "construct_prompt_with_context",
            "llm.generate_answer",
            "postprocess_and_add_citations"
        ],
        "top_docs": [
            {"doc_id": "1", "snippet": "Best sowing period for rice in Zone X is June-July", "source": "ICAR"}
        ],
        "answer": "This is a placeholder. Replace with real RAG output."
    }

@app.get("/retrieve/{doc_id}")
async def retrieve(doc_id: str):
    """
    Return a document from the data store (placeholder).
    """
    return {"doc_id": doc_id, "text": "Document text (placeholder)", "source": "sample"}
