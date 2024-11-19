from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Pydantic Model for Books
class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int
    description: str | None = None

# In-memory database (for demonstration purposes)
books_db = []

# 1. GET: Retrieve all books
@app.get("/books", response_model=List[Book])
def get_books():
    return books_db

# 2. GET: Retrieve a book by ID
@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    book = next((book for book in books_db if book.id == book_id), None)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

# 3. POST: Add a new book
@app.post("/books", response_model=Book)
def add_book(book: Book):
    # Check if book ID already exists
    if any(b.id == book.id for b in books_db):
        raise HTTPException(status_code=400, detail="Book with this ID already exists")
    books_db.append(book)
    return book

# 4. PUT: Update an existing book
@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, updated_book: Book):
    for idx, book in enumerate(books_db):
        if book.id == book_id:
            books_db[idx] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")

# 5. DELETE: Remove a book
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    global books_db
    books_db = [book for book in books_db if book.id != book_id]
    return {"message": f"Book with ID {book_id} deleted successfully"}
