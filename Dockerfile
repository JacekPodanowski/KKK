FROM python:3.12

ENV PYTHONUNBUFFERED=1

RUN mkdir /app

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

CMD ["python", "main.py"]