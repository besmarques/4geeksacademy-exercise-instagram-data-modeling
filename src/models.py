import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

#class Person(Base):
#    __tablename__ = 'persondsasdasd'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
#    id = Column(Integer, primary_key=True)
#    name = Column(String(250), nullable=False)

#class Address(Base):
#    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
#    id = Column(Integer, primary_key=True)
#    street_name = Column(String(250))
#    street_number = Column(String(250))
#    post_code = Column(String(250), nullable=False)
#    person_id = Column(Integer, ForeignKey('person.id'))
#    person = relationship(Person)

class Local(Base):
    __tablename__ = 'local'
    id = Column(Integer, primary_key=True)
    coordinates = Column(Integer, nullable=False)

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)

class Posts(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    date_posted = Column(String(250), nullable=False)
    local_id = Column(Integer, ForeignKey('local.id'))
    local = relationship(Local)
    media_id = Column(Integer, ForeignKey('media.id'))
    media = relationship(Media)
    

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    posts_id = Column(Integer, ForeignKey('posts.id'))
    posts = relationship(Posts)


class Sugestions(Base):
    __tablename__ = 'sugestions'
    id = Column(Integer, primary_key=True)
    sugestion = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)


class Comments(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    text = Column(String, ForeignKey('local.id'))
    author = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    post_id = Column(Integer, ForeignKey('posts.id'))
    post = relationship(Posts)

class Likes(Base):
    __tablename__ = 'likes'
    id = Column(Integer, primary_key=True)
    text = Column(String, ForeignKey('local.id'))
    author = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    post_id = Column(Integer, ForeignKey('posts.id'))
    post = relationship(Posts)

class Followers(Base):
    __tablename__ = 'follow'
    id = Column(Integer, primary_key=True)
    follower_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    following_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Saved(Base):
    __tablename__ = 'saved'
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    post_id = Column(Integer, ForeignKey('posts.id'))
    post = relationship(Posts)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e