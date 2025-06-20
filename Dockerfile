FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir fastapi uvicorn

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
