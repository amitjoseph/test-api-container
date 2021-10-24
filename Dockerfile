FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000
ENV GUNICORN_CMD_ARGS="--bind=0.0.0.0 --chdir=./src/"
CMD [ "gunicorn", "app:app" ]