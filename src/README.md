1) Ingest & index
   - Parse CSV/docs -> clean text, metadata
   - Create embeddings (sentence-transformers) for each doc
   - Index embeddings in FAISS

2) Query flow (/ask)
   - User query -> embed(query)
   - faiss.search(query_embedding, top_k) -> top_docs
   - Build prompt: system + instruction + top_docs (with citations) + user query
   - Call LLM (local HF + temperature=0.0 for deterministic)
   - Postprocess: extract citations, confidence, provenance

3) /retrieve
   - Return full document by id, with metadata and source link

Minimal pseudocode:
embed = embed_model.encode(query)
ids, scores = faiss_index.search(embed, k=top_k)
context = "\n\n".join([format_doc(d) for d in load_docs(ids)])
prompt = build_prompt(context, query)
answer = llm.generate(prompt)
return {"answer": answer, "source_docs": ids, "scores": scores}
