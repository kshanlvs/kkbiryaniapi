from sqlalchemy import Column, Integer, String, Text, ForeignKey, Boolean, DECIMAL, TIMESTAMP
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(15), unique=True, nullable=False)
    address = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)

class Restaurant(Base):
    __tablename__ = 'restaurants'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    location = Column(Text, nullable=False)
    contact_number = Column(String(15), nullable=True)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)

class MenuItem(Base):
    __tablename__ = 'menu_items'
    id = Column(Integer, primary_key=True, index=True)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    name = Column(String(100), nullable=False)
    description = Column(Text)
    price = Column(DECIMAL(10, 2), nullable=False)
    is_available = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    total_amount = Column(DECIMAL(10, 2), nullable=False)
    status = Column(String(50), default='Pending')
    created_at = Column(TIMESTAMP, default=datetime.utcnow)

class OrderItem(Base):
    __tablename__ = 'order_items'
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    menu_item_id = Column(Integer, ForeignKey('menu_items.id'))
    quantity = Column(Integer, nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
