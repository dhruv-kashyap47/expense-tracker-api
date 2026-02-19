# Expense Tracker API

FastAPI-based Expense Tracker with CRUD operations, filtering, and total calculation.

## Run Locally

uvicorn main:app --reload

## Endpoints

POST /expenses
GET /expenses
GET /expenses/{id}
GET /expenses/category/{category}
GET /expenses/total
PUT /expenses/{id}
DELETE /expenses/{id}
