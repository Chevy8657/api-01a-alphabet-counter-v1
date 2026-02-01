from fastapi import FastAPI, Query
from pydantic import BaseModel
import re

app = FastAPI(title="Alphabet Counter", version="v1")

class Health(BaseModel):
    ok: bool

class AlphabetCountResponse(BaseModel):
    input: str
    alphabet_count: int

@app.get("/health", response_model=Health)
def health():
    return {"ok": True}

@app.get("/v1/alphabet-count", response_model=AlphabetCountResponse)
def alphabet_count(text: str = Query(..., description="Text to count alphabetic characters for")):
    letters = re.findall(r"[A-Za-z]", text)
    return {"input": text, "alphabet_count": len(letters)}
