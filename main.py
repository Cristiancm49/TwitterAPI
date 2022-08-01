#Python
from datetime import date
from typing import Optional, List
from uuid import UUID
from datetime import datetime


#Pydantic
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field

#FastAPI 
from fastapi import FastAPI
from fastapi import status

app = FastAPI()

# Models
class UserBase(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)


class UserLogin(UserBase):
    password: str = Field(
        ...,
        min_length=8,
        max_length=64
    )


class User(UserBase):

    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    birth_date: Optional[date] = Field(default=None)


class tweet(BaseModel):
    tweet_id: UUID = Field(...)
    content: str = Field(
        ...,
        min_length=1,
        max_length=256
    )
    create_at: datetime = Field(default=datetime.now())
    update_at: Optional[datetime] = Field(default=None)
    by: User = Field(...)


# Path Operations

@app.get(path="/")
def home():
    return {"Twitter API":"Working!"}

## Users

@app.post(
    path="/signup",
    response_model= User,
    status_code=status.HTTP_201_CREATED,
    summary="Registro de usuario",
    tags=["Users"]
)
def signup():
    pass


@app.post(
    path="/login",
    response_model= User,
    status_code=status.HTTP_200_OK,
    summary="Login de usuario",
    tags=["Users"]
)
def login():
    pass


@app.get(
    path="/users",
    response_model= List[User],
    status_code=status.HTTP_200_OK,
    summary="Muestra todos los usarios",
    tags=["Users"]
)
def mostrar_todos_los_usuarios():
    pass


@app.get(
    path="/users/{user_id}",
    response_model= User,
    status_code=status.HTTP_200_OK,
    summary="Mostrar usuario",
    tags=["Users"]
)
def mostrar_usuario():
    pass


@app.delete(
    path="/users/{user_id}/delete",
    response_model= User,
    status_code=status.HTTP_200_OK,
    summary="Eliminar usuario",
    tags=["Users"]
)
def eliminar_usuario():
    pass

@app.put(
    path="/users/{user_id}/update",
    response_model= User,
    status_code=status.HTTP_200_OK,
    summary="actualizar usuario",
    tags=["Users"]
)
def actualizar_usuario():
    pass


## Tweets



