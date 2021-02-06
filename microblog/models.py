from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from user.models import User

from core.db import Base

class Post(Base):
    __tablename__ = "microblog_posts"
    id = Column(Integer, primary_key = True, index = True, unique = True)
    title = Column(String)
    text = Column(String(length=350))
    date = Column(DateTime)
    user = Column(Integer, ForeignKey("user.id"))
    user_id = relationship(User)