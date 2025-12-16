from itertools import product
from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator
import re

app = FastAPI()

pioneer = [
    product(
        name='Кредит 100% годовых',
        description='Идеально для того что бы стать нищим'
    ),
    product(
        id=2,
        name='Кредит 50% годовых',
        discription='Идеально для терпения'
    )
]
repeater = []

class UserRequest(BaseModel):
    name: str
    phone: str
    email: str = None

    @field_validator('phone')
    def valifator_phone(cls, v):

        if len(v) < 10:
            raise ValueError('Номер телефона слишком короткий')
        
        if len(v) > 11:
            raise ValueError('Номер телефона слишком длинный')
         
        if v.startswith('8'):
            v = '7' + v[1:]

        return v

clients_db = {}

@app.post('/register')
async def register_user(user: UserRequest):

    # clients_db[user.phone] = register_user

    if user.phone in clients_db:
        return repeater
    
    clients_db[user.phone] = {
        "phone": user.phone,
        "name": user.name
    }
    return pioneer


        



 