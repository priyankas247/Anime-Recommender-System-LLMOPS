import os
from dotenv import load_dotenv
load_dotenv()
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
MODEL_NAME = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")
print("DEBUG -> GROQ_API_KEY:", GROQ_API_KEY)
print("DEBUG -> MODEL_NAME:", MODEL_NAME)