#Python
import json
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
from fastapi import Body

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


class UserRegister(User):
        password: str = Field(
        ...,
        min_length=8,
        max_length=64
    )


class Tweet(BaseModel):
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

## Users

### Registrar un usuario
@app.post(
    path="/signup",
    response_model= User,
    status_code=status.HTTP_201_CREATED,
    summary="Registro de usuario",
    tags=["Users"]
)
def signup(user: UserRegister = Body(...)):
    """
    REGISTRO DE USUARIO

    Esta path operation registra un usuario en la aplicacion

    Parameters:
     -Request body parameter
      - user: UserRegister

    Return Json con la informacion basica d eun usuario:
     - user_id: UUID
     - email: Emailstr
     - firt_name: str
     - last_name: str
     - birth_date: date
    """
    with open("users.json", "r+", encoding="utf-8") as f:
        results = json.loads(f.read())
        user_dict = user.dict()
        user_dict["user_id"]= str(user_dict["user_id"])
        user_dict["birth_date"]= str(user_dict["birth_date"])
        results.append(user_dict)
        f.seek(0)
        f.write(json.dumps(results))
        return user 

### Ingreso de un usuario
@app.post(
    path="/login",
    response_model= User,
    status_code=status.HTTP_200_OK,
    summary="Login de usuario",
    tags=["Users"]
)
def login():
    pass


### Mostrar todos los usuarios
@app.get(
    path="/users",
    response_model= List[User],
    status_code=status.HTTP_200_OK,
    summary="Muestra todos los usarios",
    tags=["Users"]
)
def mostrar_todos_los_usuarios():
    """
    MOTRAR TODOS LOS USUARIOS

    Esta path parameter muestra a todos los usuarios de la aplciacion

    Parameters:
     -

    Returns:
    Retorna un Json con todos los usuarios de la app, seguido de las siguientes llaves
     - user_id: UUID
     - email: Emailstr
     - firt_name: str
     - last_name: str
     - birth_date: date

    """
    with open("users.json", "r", encoding="utf-8") as f:
       results = json.loads(f.read()) 
       return results

### Mostrar un usuario
@app.get(
    path="/users/{user_id}",
    response_model= User,
    status_code=status.HTTP_200_OK,
    summary="Mostrar usuario",
    tags=["Users"]
)
def mostrar_usuario():
    pass


### Eliminar un usuario
@app.delete(
    path="/users/{user_id}/delete",
    response_model= User,
    status_code=status.HTTP_200_OK,
    summary="Eliminar usuario",
    tags=["Users"]
)
def eliminar_usuario():
    pass


### Actualizar un usuario
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
### Mostrar todos los tweets
@app.get(
    path="/",
    response_model= list[Tweet],
    status_code=status.HTTP_200_OK,
    summary="Todos los tweets",
    tags=["Tweets"]
    )
def home():
    return {"Twitter API":"Working!"}


### Crear un tweet
@app.post(
    path="/post",
    response_model= Tweet,
    status_code=status.HTTP_201_CREATED,
    summary="Crear un tweet",
    tags=["Tweets"]
)
def crear_un_tweet():
    pass


### Mostrar un tweet
@app.get(
    path="/tweets/{tweet.id}",
    response_model= Tweet,
    status_code=status.HTTP_200_OK,
    summary="Mostrar un tweet",
    tags=["Tweets"]
)
def mostrar_un_tweet():
    pass


### Eliminar un tweet
@app.delete(
    path="/tweets/{tweet.id}/delete",
    response_model= Tweet,
    status_code=status.HTTP_200_OK,
    summary="Eliminar un tweet",
    tags=["Tweets"]
)
def eliminar_un_tweet():
    pass


### Actualizar un tweet
@app.put(
    path="/tweets/{tweet.id}/update",
    response_model= Tweet,
    status_code=status.HTTP_200_OK,
    summary="Actualizar un tweet",
    tags=["Tweets"]
)
def actualizar_un_tweet():
    pass

