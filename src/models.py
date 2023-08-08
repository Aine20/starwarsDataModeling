import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    email = Column(String(20), nullable=False)
    password = Column(String(20), nullable=False)

class Favorite(Base):
    __tablename__ = 'favorite'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    characters = Column(String(20))
    planets = Column(String(20))

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(20), ForeignKey('favorite.characters'))
    birth_day = Column(String(20))
    gender = Column(String(20))
    height = Column(Integer)
    skin_color = Column(String(20))
    eye_color = Column(String(20))


class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(20), ForeignKey('favorite.planets'))
    climate = Column(String(20))
    population = Column(Integer)
    terrain = Column(String(20))
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    diameter = Column(Integer)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')