from fastapi import FastAPI
from app.controllers.student_controller import router 

from app.config.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FastAPI Template",
    version="1.0"
)

app.include_router(router)

app.get("/")
def myhome():
    return {"message": "Welcome to FastAPI Template!"}