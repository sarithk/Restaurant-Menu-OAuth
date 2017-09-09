import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
    """User table class"""
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))

class Restaurant(Base):
    """Restaurant table class"""
    # def __init__(self, arg):
    #     super(ClassName, self).__init__()
    #     self.arg = arg
    __tablename__ = 'restaurant'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)


class MenuItem(Base):
    """Menu item table class"""
    __tablename__ = 'menu_item'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    description = Column(String(250))
    price = Column(String(8))
    course = Column(String(250))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    

    @property
    def serialize(self):
    # Returns object data in serialized format
     return {
        'name':self.name,
        'description':self.description,
        'id':self.id,
        'price':self.price,
        'course':self.course
        }

###insert at end of file######
engine = create_engine('sqlite:///restaurantmenuwithusers.db')
Base.metadata.create_all(engine)

