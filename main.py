from typing import List
from uuid import uuid4, UUID

from fastapi import FastAPI

from models import User, Gender, Role

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
