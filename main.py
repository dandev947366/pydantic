from fastapi import FastAPI

app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    
    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
    
BOOKS = [
    Book(1, 'Computer Science Pro', 'Tom', 'A very good book', 5),
    Book(2, 'Fundamentals of Data Engineering:', 'Joe Reis', 'nice good book', 4),
    Book(3, 'Measure What Matters', 'John Doerr', 'Well written book', 4.5),
    Book(4, 'Radical Focus (Second Edition)', 'Christina Wodtke', 'informative book', 4.3),
    Book(5, 'Continuous Discovery Habits', 'Teresa Torres', 'well structed', 4.7),
    Book(6, 'Jobs to Be Done: Theory to Practice', 'Anthony W. Ulwick', 'A very good book', 4),
    Book(7, 'User Story Mapping', 'Jeff Patton ', 'A very great book', 4.5),
    Book(8, 'Design a Better Business', 'Patrick van der Pijl ', 'nice to read book', 4.1),
]



@app.get("/books")
async def read_all_books():
    return BOOKS