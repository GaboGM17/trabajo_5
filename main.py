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
