FROM python:3.8-slim-buster

WORKDIR /app

COPY server.py .

EXPOSE 8000

CMD ["python", "server.py"]
