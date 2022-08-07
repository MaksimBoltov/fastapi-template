from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from app.database import get_db

app = FastAPI()

# Handlers or include routers
# app.include_router(router, prefix="prefix", tags=["tag"])


@app.get('/')
def hello(db: Session = Depends(get_db)):
    return 'Hello, World!'
