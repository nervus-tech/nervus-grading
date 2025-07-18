from fastapi import FastAPI
from contextlib import asynccontextmanager
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models.grade import Base, Grade
import logging

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    db = SessionLocal()
    try:
        # Create tables
        Base.metadata.create_all(bind=engine)
        # Check if data exists
        if db.query(Grade).count() == 0:
            # Seed sample grades
            grade1 = Grade(student_id=1, assignment_id=1, score=85)
            grade2 = Grade(student_id=2, assignment_id=2, score=92)
            db.add(grade1)
            db.add(grade2)
            db.commit()
            logger.info("Seeded 2 grades into grades")
        else:
            logger.info("Grades already seeded, skipping...")
        yield
    finally:
        db.close()

app = FastAPI(lifespan=lifespan)

@app.get("/test")
def read_root():
    return {"message": "Grading Service is running"}