# Используем базовый образ с Python
FROM apify/actor-python:3.13

# Устанавливаем зависимости
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Копируем код скрипта
COPY . /src/

# Делаем скрипт исполнимым
RUN python3 -m compileall -q .

# Запуск скрипта для авторизации и получения cookies
CMD ["python3", "-m", "src"]
