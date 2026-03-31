# CI/CD Optimized DevOps Project

## Overview
This project demonstrates a CI/CD pipeline using GitHub Actions, Docker, and AWS (ECR + ECS).

## App
Simple FastAPI Order Processing API.

## Endpoints
- GET /health
- POST /order

## Run Locally
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Docker
```bash
docker build -t app .
docker run -p 8000:8000 app
```

## CI/CD Flow
- PR → CI checks
- Merge → build + push to ECR
- Deploy → ECS

## Notes
Replace <YOUR_ECR_URI> before deployment.
