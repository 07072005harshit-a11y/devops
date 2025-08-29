FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install flask pytest

CMD ["python", "flask1.py"]
