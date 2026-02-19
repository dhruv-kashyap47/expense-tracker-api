## 🚀 Expense Tracker API (FastAPI)

A backend REST API built using **FastAPI** for managing daily expenses with full CRUD functionality, category-based filtering, and total expense calculation.

This project focuses on clean backend architecture, proper HTTP status handling, and real-world API design patterns.

---

### ✨ Features

* Create, read, update, and delete expenses
* Filter expenses by category
* Calculate total spending dynamically
* Input validation using Pydantic models
* Proper HTTP status codes & error handling

---

### 🛠 Tech Stack

* FastAPI
* Python
* Pydantic
* Uvicorn

---

### ▶ How to Run Locally

```bash
pip install fastapi uvicorn
uvicorn main:app --reload
```

Open in browser:

```
http://127.0.0.1:8000/docs
```

---

### 📡 API Endpoints

| Method | Endpoint                      | Description        |
| ------ | ----------------------------- | ------------------ |
| POST   | /expenses                     | Create expense     |
| GET    | /expenses                     | Get all expenses   |
| GET    | /expenses/{id}                | Get expense by ID  |
| GET    | /expenses/category/{category} | Filter by category |
| GET    | /expenses/total               | Get total spending |
| PUT    | /expenses/{id}                | Update expense     |
| DELETE | /expenses/{id}                | Delete expense     |

---

### 🎯 Purpose

This project was built to strengthen backend fundamentals including:

* REST API design
* Data validation
* Business logic handling
* Error management

