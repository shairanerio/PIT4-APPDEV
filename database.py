import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

database_url = os.environ.get("vitePostgresql")

if not database_url:
    raise ValueError("DATABASE_URL environment variable not set")

engine = create_engine(database_url, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()