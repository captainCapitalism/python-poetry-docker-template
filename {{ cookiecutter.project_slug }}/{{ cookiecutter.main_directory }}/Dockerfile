FROM python:{{ cookiecutter.python_version }}-slim

RUN apt-get update
RUN apt install curl -y

ENV \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PIP_NO_CACHE_DIR=off \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_HOME=/py-poetry \
  POETRY_VIRTUALENVS_CREATE=0 \
  POETRY_VERSION={{ cookiecutter.python_poetry_version }}


RUN curl -sSL https://install.python-poetry.org/ | python
ENV PATH="${POETRY_HOME}/bin:$PATH"

COPY pyproject.toml poetry.lock ./

RUN poetry install

COPY . .