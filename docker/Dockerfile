FROM python:3.7-slim AS BUILDER
WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt
RUN rm -f requirements.txt

# Distroless python3
FROM gcr.io/distroless/python3-debian10
COPY --from=BUILDER /app /app
COPY --from=BUILDER /usr/local/lib/python3.7/site-packages /usr/lib/python3.7/site-packages

ARG FLASK_APP=/app/run.py
ENV FLASK_APP=$FLASK_APP

ARG FLASK_ENV=development
ENV FLASK_ENV=$FLASK_ENV

ENV PYTHONUNBUFFERED=True
ENV PYTHONPATH=/usr/lib/python3.7/site-packages

WORKDIR /app
COPY . /app

VOLUME /app
EXPOSE 8080

CMD ["-m", "flask", "run", "-h", "0.0.0.0", "-p", "8080"]