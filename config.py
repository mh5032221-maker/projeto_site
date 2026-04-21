import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = "super_secret_key"
    DATABASE_URL = os.getenv("DATABASE_URL")