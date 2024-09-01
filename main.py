from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app=FastAPI()

blogs = [
    "Hey this is blog 1",
    "Hey this is blog 2",
    "Hey this is blog 3",
    "Hey this is blog 4",
    ]
@app.get("/")
def say_hello():
    return "Fastapi biyatch"

@app.get("/blogs/{id}")
def show_blog(id : int):
    return {"data" : blogs[id]}

class Blog(BaseModel):
    title: str
    description: str
    published: Optional[bool]

@app.post("/blogs")
def post_method(blog: Blog):
    return f"Blog is created with title as {blog.title}"

if __name__=="__main__":
    app.run()
    
