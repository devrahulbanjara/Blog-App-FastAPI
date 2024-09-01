from fastapi import FastAPI

from blog import models, database, schemas

models.Base.metadata.create_all(bind=database.engine)

app=FastAPI()
 

@app.post("/blog")
def create(request : schemas.Blog):
    return request