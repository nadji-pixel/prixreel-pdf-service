FROM ghcr.io/weasyprint/weasyprint:latest

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir flask gunicorn

COPY app.py .

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--timeout", "120", "app:app"]
