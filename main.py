import os
from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from typing import List, Literal

from chat import getResponse

load_dotenv()

CLIENT_URL = os.getenv("CLIENT_URL")
print(CLIENT_URL)
app = FastAPI()

# allow_origins=[CLIENT_URL], 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatMessage(BaseModel):
    role: Literal["user", "assistant"]
    content: str

class ChatRequest(BaseModel):
    message: List[ChatMessage]

@app.post("/chat/{persona}")
async def chat(persona:str, input:ChatRequest):
    return getResponse(persona, input.message)
