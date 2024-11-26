from typing import Union
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.initdabase import initialize_database
from app.models import User

# Create the FastAPI app instance
app = FastAPI()


# FastAPI event to initialize the database on application startup
@app.on_event("startup")
async def startup_event():
    initialize_database()


@app.post("/users/register")
def register_user(name: str, email: str, phone_number: str, db: Session = Depends(SessionLocal)):
    user = User(name=name, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"message": "User registered successfully", "user_id": user.id}


# Run the application when the script is executed directly
if __name__ == "__main__":
    import uvicorn

    # Optional: Call the initialize_database() here if it's critical before starting the server
    # initialize_database()

    # Start the FastAPI server
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
