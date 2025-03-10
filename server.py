from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import subprocess

app = FastAPI()

# ✅ CORS 설정 추가 (React에서 FastAPI로 요청 가능하게 허용)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React 주소 허용
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메서드 허용 (GET, POST 등)
    allow_headers=["*"],  # 모든 헤더 허용
)

class Question(BaseModel):
    query: str

@app.post("/ask")
async def ask_question(question: Question):
    result = subprocess.run(["ollama", "run", "farm-ai", question.query], capture_output=True, text=True)
    return {"response": result.stdout.strip()}
