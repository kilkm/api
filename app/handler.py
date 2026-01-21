from fastapi import FastAPI
from pydantic import BaseModel, field_validator
import re

app = FastAPI()

pioneer = [
    {'name':'Кредит 100% годовых', 'description':'Идеально для того что бы стать нищим'},
    {'name':'Кредит 50% годовых', 'description':'Идеально для терпения'},
    {'name':'Кредит 20% годовых', 'description':'Для своих'}
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
        
        elif len(v) > 12:
            raise ValueError('Номер телефона слишком длинный')
         
        elif v.startswith('8'):
            v = '7' + v[1:]

        elif v.startswitch('+7'):
            v = '7' + v[1:]

        return v

clients_db = {}

@app.post('/register')
async def register_user(user: UserRequest):

    if user.phone in clients_db:
        return repeater
    
    clients_db[user.phone] = {
        "phone": user.phone,
        "name": user.name
    }
    return pioneer


        



 