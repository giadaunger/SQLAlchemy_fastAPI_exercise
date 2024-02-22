from fastapi import FastAPI, HTTPException, Depends, status
from app.db_setup import init_db, get_db
from contextlib import asynccontextmanager
from fastapi import Request
from sqlalchemy.orm import Session, joinedload, selectinload
from sqlalchemy import select, update, delete, insert
from app.database.models import Company
from app.database.schemas import CompanySchema, CompanyType


# Funktion som körs när vi startar FastAPI - 
# perfekt ställe att skapa en uppkoppling till en databas
@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db() # Vi ska skapa denna funktion
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/company", status_code=200)
def list_companies(db: Session = Depends(get_db)):
    programs = db.scalars(select(Company)).all()
    if not programs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No companies found")
    return programs

@app.post("/company", status_code=201)
def add_company(company: CompanySchema, db: Session = Depends(get_db)) -> CompanySchema:
    db_company = Company(**company.model_dump()) # **data.dict() deprecated
    db.add(db_company)
    db.commit()
    db.refresh(db_company) # Vi ser till att vi får den uppdaterade versionen med ID't
    return db_company