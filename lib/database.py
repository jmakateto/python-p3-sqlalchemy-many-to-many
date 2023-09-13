# database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

DATABASE_URL = "sqlite:///sqlite.db"  

#  database engine
engine = create_engine(DATABASE_URL)

#  tables based on the models
Base.metadata.create_all(engine)

#  session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()
