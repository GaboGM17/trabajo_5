from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uuid

app = FastAPI()


# Modelo para el usuario
class User(BaseModel):
    username: str
    email: str
    password: str


# Modelo para las tareas
class Task(BaseModel):
    title: str
    description: str
    status: str


# Base de datos simulada
users = {}
tasks = {}


# API para registrar usuarios
@app.post("/register/")
async def register_user(user: User):
    user_id = str(uuid.uuid4())
    users[user_id] = user.dict()
    return {"message": "User registered successfully", "user_id": user_id}


# API para obtener datos de usuario
@app.get("/user/{user_id}")
async def get_user(user_id: str):
    user = users.get(user_id)
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")


# API para crear tareas
@app.post("/tasks/create/")
async def create_task(task: Task, user_id: str):
    if user_id in users:
        task_id = str(uuid.uuid4())
        task_dict = task.dict()
        task_dict["user_id"] = user_id
        tasks[task_id] = task_dict
        return {"message": "Task created successfully", "task_id": task_id}
    raise HTTPException(status_code=404, detail="User not found")


# API para listar tareas por usuario
@app.get("/tasks/{user_id}")
async def get_tasks_by_user(user_id: str):
    user_tasks = [task for task in tasks.values() if task["user_id"] == user_id]
    if user_tasks:
        return user_tasks
    raise HTTPException(status_code=404, detail="No tasks found for this user")