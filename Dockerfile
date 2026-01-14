FROM python:3.11-slim

WORKDIR /app

COPY app.py /app/app.py

# créer le dossier logs dans l'image (au cas où)
RUN mkdir -p /app/logs

ENV PYTHONUNBUFFERED=1

CMD ["python3", "/app/app.py"]
