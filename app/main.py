from fastapi import FastAPI
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "FastAPI Backend"


settings = Settings()
app = FastAPI()


@app.get("/")
async def root():
    return {"message": f"Hello from {settings.app_name}"}
