FROM python:3.10-buster

COPY requirements/backend.in .
RUN python -m  venv .venv
RUN pip install -r backend.in

COPY build build
COPY spaceship spaceship


CMD ["uvicorn", "spaceship.main:app", "--host=0.0.0.0", "--port=8080"]
