# Используем образ с Python
FROM python:3

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем исходный код в контейнер
COPY length comparison.py /app/length comparison.py

# Запускаем приложение при старте контейнера
CMD ["python","/app/length comparison.py"]