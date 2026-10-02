# AI IT Request Assistant

AI-ассистент для первичного анализа IT-заявок.

## Запуск

Создать .env на основе .env.example и заполнить ключи.

Затем:

docker build -t ai-it-request-assistant .
docker run --env-file .env -p 8000:8000 ai-it-request-assistant

## Проверка

GET http://localhost:8000/health

Ожидаемый результат:

{"status": "ok", "service": "AI IT Request Assistant"}

## Переменные окружения

OPENAI_API_KEY
LANGFUSE_PUBLIC_KEY
LANGFUSE_SECRET_KEY
LANGFUSE_HOST

Секретные значения не хранятся в репозитории.