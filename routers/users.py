from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class User(BaseModel):
    id: int
    name: str
    tlf: int
    email: str

users_list = [
    User(id=1, name="charon51", tlf=123, email="charon51@yamal.com"),
    User(id=2, name="charon41", tlf=456, email="charon41@yamal.com"),
    User(id=3, name="charon31", tlf=789, email="charon31@yamal.com")
    ]

@router.get("/users")
async def users():
    return users_list

# path 
@router.get("/users/{id}")
async def users(id: int):
    user = filter(lambda user: user.id == id, users_list)
    try:
        return list(user)[0]
    except:
        return {"error": "User Not Found"}

def search_user(id: int):
    user = filter(lambda user: user.id == id, users_list)
    try:
        return list(user)[0]
    except:
        return {"error": "User Not Found"}

@router.get("/user/") # Query
async def users(id: int):
    return search_user(id)

# CREATE USER
@router.post("/user/")
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail="User already exist")
    else:
        users_list.append(user)
# {"id": 11, "name": "charon511", "tlf": 1231, "email": "charon511@yamal.com"}

@router.put("/user/")
async def user(user: User):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            return {"Success": "True"}

    if not found:
        return {"Error": "User not found"}

@router.delete("/user/{id}")
async def delete(id: int):
    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True

    if not found:
        return {"Success": "User not found"}
