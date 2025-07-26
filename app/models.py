from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime
from datetime import datetime
from .database import Base

class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(100), unique=True, index=True)
    hashed_password = Column(String(100))
    id_role = Column(Integer, ForeignKey("roles.id"))
    is_active = Column(Boolean, default=True)


    