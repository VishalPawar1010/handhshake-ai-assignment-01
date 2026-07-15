# Approved base, pinned by digest. Resolve the real digest locally (this sandbox
# can't reach Docker Hub) with:
#   docker pull python:3.13-slim-bookworm
#   docker inspect --format='{{index .RepoDigests 0}}' python:3.13-slim-bookworm
# then replace the placeholder below.
FROM python:3.13-slim-bookworm@sha256:de89ed8283721548f7f9c8acfd19d638f435fa3870693a017890e94be5d37fc6

RUN pip install --no-cache-dir pytest==8.4.1 pytest-json-ctrf==0.3.5

WORKDIR /app

COPY access.log /app/access.log