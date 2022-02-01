from typing import List
from uuid import uuid4, UUID

from fastapi import FastAPI, HTTPException

from models import User, Gender, Role, UserUpdateRequest

app = FastAPI()

db: List[User] = [
    User(
        id=UUID('6905bc5e-c898-4ce2-afd3-625a4bd28426'),
        first_name="Jamila",
        last_name="ahmed",
        gender=Gender.female,
        roles=[Role.student]
    ),
    User(
        id=UUID('3c30b5cb-38a0-4d70-9bb2-7f41b61df491'),
        first_name="Alex",
        last_name="Jones",
        gender=Gender.male,
        roles=[Role.admin, Role.user]
    ),
]


@app.get('/')
async def root():
    return {
        "hello": "me"
    }


@app.get('/api/v1/users')
async def fetch_users():
    return db


@app.post('/api/v1/users')
async def register_user(user: User):
    db.append(user)
    return {'id': user.id}


@app.delete('/api/v1/users/{user_id}')
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return f'user with id {user_id} has been deleted.'
    raise HTTPException(
        status_code=404,
        detail=f'user with id {user_id} dose not exists.'
    )


@app.put('/api/v1/users/{user_id}')
async def update_user(user_update: UserUpdateRequest, user_id: UUID):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name
            if user_update.roles is not None:
                user.roles = user_update.roles
            return f'user with id {user_id} has been updated.'
        raise HTTPException(
            status_code=404,
            detail=f'user with id {user_id} dose not exists.'
        )
