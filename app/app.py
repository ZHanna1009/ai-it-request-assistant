
from fastapi import FastAPI
from pydantic import BaseModel

from app.agent import create_project_agent
from app.state import save_request

app = FastAPI(title="AI IT Request Assistant")

agent = create_project_agent()


class RequestInput(BaseModel):
    question: str


@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "AI IT Request Assistant"
    }


@app.post("/predict")
def predict(request: RequestInput):
    result = agent.invoke({
        "messages": [
            {"role": "user", "content": request.question}
        ]
    })

    answer = result["messages"][-1].content

    save_request(
        question=request.question,
        answer=answer
    )

    return {
        "answer": answer
    }
