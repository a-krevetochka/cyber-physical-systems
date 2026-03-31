import requests
import json
import csv
from datetime import datetime

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen2.5:0.5b"

QUERIES = [
    "What is 2 + 2?",
    "What color is the sky?",
    "Name the days of the week.",
    "What is the capital of Germany?",
    "How many months are in a year?",
    "What animal says 'meow'?",
    "What is water made of?",
    "Name one planet in our solar system.",
    "What language do people speak in Japan?",
    "How many legs does a spider have?",
]


def query_ollama(prompt: str, model: str = MODEL_NAME) -> str:
    """
    Отправляет запрос на сервер Ollama и возвращает ответ модели.

    Аргументы:
        prompt (str): Текст запроса к LLM.
        model (str): Название модели для инференса.

    Возвращает:
        str: Сгенерированный ответ от LLM.
    """
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(OLLAMA_URL, json=payload)
    response.raise_for_status()
    return response.json()["response"].strip()


def run_inference(queries: list) -> list:
    """
    Прогоняет список запросов через модель и собирает результаты.

    Аргументы:
        queries (list): Список строк-запросов к LLM.

    Возвращает:
        list: Список словарей с ключами 'query' и 'response'.
    """
    results = []
    for i, query in enumerate(queries, 1):
        print(f"[{i}/{len(queries)}] Sending: {query}")
        response = query_ollama(query)
        print(f"  → Response: {response[:80]}...\n")
        results.append({"query": query, "response": response})
    return results


def save_report(results: list, filename: str = "inference_report.csv") -> None:
    """
    Сохраняет результаты инференса в CSV-отчёт с двумя столбцами.

    Аргументы:
        results (list): Список словарей с ключами 'query' и 'response'.
        filename (str): Имя выходного CSV-файла.

    Возвращает:
        None
    """
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["query", "response"])
        writer.writeheader()
        writer.writerows(results)
    print(f"Report saved to {filename}")


if __name__ == "__main__":
    results = run_inference(QUERIES)
    save_report(results)