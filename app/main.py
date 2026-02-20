from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List

app = FastAPI()

expenses_db = []


class Expense(BaseModel):
    id : int
    title : str
    amount : float
    category: str
    date: str

# create expense
@app.post("/expenses", status_code= status.HTTP_201_CREATED)
def create_expense(expense : Expense):
    for item in expenses_db:
        if item.id == expense.id:
            raise HTTPException(
                status_code=400,
                detail="Expense with this ID already exists"
            )
    expenses_db.append(expense)
    return expense

# get all expenses
@app.get("/expenses", response_model=List[Expense])
def get_expenses():
    return expenses_db

# get total amount spent
@app.get("/expenses/total")
def get_total():
    total = 0

    for expense in expenses_db:
        total = total + expense.amount

    return {"total_spent": total}

#get expense by id
@app.get("/expenses/{id}")
def get_expense(id : int):
    for item in expenses_db:
        if item.id == id:
            return item

    raise HTTPException(
        status_code=404,
        detail="Expense not found"
    )

# get expense by category
@app.get("/expenses/category/{category}")
def get_by_category(category : str):
    filtered = []
    for expense in expenses_db:
        if expense.category.lower() == category.lower():
            filtered.append(expense)

    if not filtered:
         raise HTTPException(
                status_code=404,
                detail="No expenses found in this category"
            )

    return filtered

# update expense
@app.put("/expenses/{id}")
def update_expense(id : int, updated : Expense):
    for index, expense in enumerate(expenses_db):
        if expense.id == id:
            expenses_db[index] = updated
            return updated

    raise HTTPException(
        status_code=404,
        detail="Expense not found"
    )

# delete expense
@app.delete("/expenses/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_expense(id : int):
    for expense in expenses_db:
        if expense.id == id:
            expenses_db.remove(expense)
            return

    raise HTTPException(
        status_code=404,
        detail="Expense not found"
    )


