from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .configuration import Config

engine = create_engine(Config.SQL_ALCHEMY_DATABASE_URI, echo=True)
orm_session = sessionmaker(bind=engine)
