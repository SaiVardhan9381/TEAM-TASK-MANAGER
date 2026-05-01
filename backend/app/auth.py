from jose import jwt
from datetime import datetime, timedelta

SECRET = "secret"

def create_token(data: dict):
    return jwt.encode(data, SECRET, algorithm="HS256")