![Static Badge](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![Static Badge](https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white)

## Introduction

This project sets up a microservices architecture using Docker, involving a Flask application (`flask-dummy`) that sends logs over GRPC, a log collector (`otelcollector`) that collects these logs and exports them to Loki, and Grafana for log visualization.

## Getting Started

- **Docker**: Version 19.03.0 or newer.
- **Docker Compose**: Version 1.25.0 or newer.
- Provisioning is done so you only need to run the

```
docker-compose up --build
```
