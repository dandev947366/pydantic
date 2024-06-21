from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Union

app = FastAPI()

class Book(BaseModel):
    id: int
    title: str
    author: str
    description: str
    rating: Union[int, float]  # Allow both integer and float for ratings

class BookRequest(BaseModel):
    id: int
    title: str
    author: str
    description: str
    rating: Union[int, float]

# Initialize BOOKS with instances of the Book model
BOOKS = [
    Book(id=1, title='Computer Science Pro', author='Tom', description='A very good book', rating=5),
    Book(id=2, title='Fundamentals of Data Engineering:', author='Joe Reis', description='Nice good book', rating=4),
    Book(id=3, title='Measure What Matters', author='John Doerr', description='Well written book', rating=4.5),
    Book(id=4, title='Radical Focus (Second Edition)', author='Christina Wodtke', description='Informative book', rating=4.3),
    Book(id=5, title='Continuous Discovery Habits', author='Teresa Torres', description='Well structured', rating=4.7),
    Book(id=6, title='Jobs to Be Done: Theory to Practice', author='Anthony W. Ulwick', description='A very good book', rating=4),
    Book(id=7, title='User Story Mapping', author='Jeff Patton', description='A very great book', rating=4.5),
    Book(id=8, title='Design a Better Business', author='Patrick van der Pijl', description='Nice to read book', rating=4.1),
]

@app.get("/books", response_model=List[Book])
async def read_all_books():
    return BOOKS

@app.post("/create-book", response_model=Book)
async def create_book(book_request: BookRequest):
    BOOKS.append(new_book)
    return new_book

