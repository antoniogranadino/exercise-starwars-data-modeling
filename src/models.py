import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
1
Base = declarative_base()

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key = True)
    email = Column(String(100), nullable = False)
    username = Column(String(50),nullable = False)
    password = Column(String(500), nullable = False)
    favorite =(relationship("Favorite"))
    
class Person(Base):
    __tablename__ = "person"

    id = Column(Integer, primary_key = True)
    name = Column(String(50), nullable = False)
    gender = Column(String(50), nullable = False)
    age =  Column(Integer)
    planet = Column(String(100), nullable = False)
    vehicle = (relationship("Vehicle"))
    favorite = (relationship("Favorite"))
    
class Vehicle(Base):
    __tablename__ = "vehicle"

    id = Column(Integer, primary_key = True)
    name = Column(String(50), nullable = False)
    model = Column(String(100), nullable = False)
    color = Column(String(50), nullable = False)
    person_id = Column(Integer, ForeignKey("Person.id"), nullable = False)
    favorite = (relationship("Favorite")) 
    
class Planet(Base):

    __tablename__ = "planet"

    id = Column(Integer, primary_key = True)
    name = Column(String(100), nullable = False)
    population = Column(String(100), nullable = False)
    climate = Column(String(100), nullable = False)
    land = Column(String(100), nullable = False)
    favorite = (relationship("Favorite"))


class Favorite(Base):

    __tablename__ = "favorite"

    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable = False)
    person_id = Column(Integer, ForeignKey("person.id"), nullable = False)
    planet_id = Column(Integer, ForeignKey("planet.id"), nullable = False)
    vehicle_id = Column(Integer, ForeignKey("vehicle.id"), nullable = False)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
