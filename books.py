from fastapi import FastAPI, Path, Query
from pydantic import BaseModel,Field
from typing import List, Optional

app = FastAPI()

class Book(BaseModel):
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int

class BookRequest(BaseModel):
    id: Optional[int] = None
    title: str = Field(..., min_length=3, example='A New Book')
    author: str = Field(..., min_length=3, example='A New Author')
    description: str = Field(..., min_length=3, max_length=100, example='A brief description of the new book.')
    rating: int = Field(..., gt=-1, lt=6, example=5)
    published_date: int = Field(..., gt=1999, lt=2025, example=2020)
   
BOOKS = [
    Book(id=1, title='Computer Science Pro', author='Tom', description='A very good book', rating=5, published_date=2020),
    Book(id=2, title='Fundamentals of Data Engineering:', author='Joe Reis', description='Nice good book', rating=4, published_date=2019),
    Book(id=3, title='Measure What Matters', author='John Doerr', description='Well written book', rating=4, published_date=2018),
    Book(id=4, title='Radical Focus (Second Edition)', author='Christina Wodtke', description='Informative book', rating=3,published_date=2023),
    Book(id=5, title='Continuous Discovery Habits', author='Teresa Torres', description='Well structured', rating=5,published_date=2021),
    Book(id=6, title='Jobs to Be Done: Theory to Practice', author='Anthony W. Ulwick', description='A very good book', rating=4, published_date=2015),
    Book(id=7, title='User Story Mapping', author='Jeff Patton', description='A very great book', rating=4, published_date=2012),
    Book(id=8, title='Design a Better Business', author='Patrick van der Pijl', description='Nice to read book', rating=5, published_date=2012),
]

@app.get("/books", response_model=List[Book])
async def read_all_books():
    return BOOKS
@app.get("/books/{book_id}")
async def read_book(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
            
@app.get("/books/")
async def read_book_by_rating(book_rating: int = Query(gt=0, lt=6)):
    books_by_rating = [book for book in BOOKS if book.rating == book_rating]
    return books_by_rating
    
@app.post("/create-book", response_model=Book)
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.dict())
    BOOKS.append(new_book)
    return new_book

def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book
    
@app.get("/books/publish/")
async def read_books_by_published_date(published_date: int = Query(gt=1999, lt=2025)):
    books_by_date = [book for book in BOOKS if book.published_date == published_date]
    return books_by_date
    
@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            break
    return BOOKS