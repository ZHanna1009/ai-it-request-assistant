
import json
from pathlib import Path
from datetime import datetime, timezone

STATE_FILE = Path(__file__).resolve().parent.parent / "data" / "state.json"


def load_state():
    if not STATE_FILE.exists():
        return {"requests": []}

    with open(STATE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_request(question, answer):
    state = load_state()

    state["requests"].append({
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "question": question,
        "answer": answer
    })

    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)

    return state
