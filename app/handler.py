from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator
import re

app = FastAPI()

class UserRequest(BaseModel):
    name: str
    phone: str
    email: str = None

    @field_validator('phone')
    def valifator_phone(cls, v):
        digits = re.sub(r'\D', '', v)

        if len(digits) < 10:
            raise ValueError('Номер телефона слишком короткий')
        
        if digits.startswith('8'):
            digits = '7' + digits[1:]

        return digits

@app.post('/register')
async def register_user(user: UserRequest):
    return {
        'message': 'Пользователь зарегестрирован',
        'user': {
            'name': user.name,
            'phone': user.phone,
            'email': user.email
        }
    }
