# Lab 2: NLP — Инференс Qwen2.5:0.5B через Ollama

## Требования

- Python 3.8+
- [Ollama](https://ollama.com)

---

## Развёртывание

### 1. Установить Ollama

**Linux:**
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

**Windows / macOS:** скачать установщик с [ollama.com](https://ollama.com)

### 2. Скачать модель

```bash
ollama pull qwen2.5:0.5b
```

### 3. Запустить сервер

```bash
ollama serve
```

> Сервер запустится на `http://localhost:11434`  
> Если видите ошибку `bind: Only one usage of each socket address` — сервер уже запущен, всё в порядке.

### 4. Установить зависимости Python

```bash
pip install requests
```

---

## Запуск

```bash
python inference.py
```

После выполнения в папке появится файл `inference_report.csv` с результатами инференса.

---

## Структура проекта

```
.
├── inference.py          # Основной скрипт
└── inference_report.csv  # Отчёт (генерируется после запуска)
```

---

## Пример вывода

```
Запуск инференса...

[1/10] Отправка: What is 2 + 2?
  → Ответ: 2 + 2 = 4...

[2/10] Отправка: What color is the sky?
  → Ответ: The sky is blue...

...

Отчёт сохранён в inference_report.csv
```