#!/usr/bin/python3
""" a class to sophisticate console """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from models.review import Review
from os import getenv

storage_type = getenv("HBNB_TYPE_STORAGE")


class Place(BaseModel, Base):
    """Place class that inherits from BaseModel."""
    __tablename__ = "places"
    if storage_type == "db":
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship("Review", cascade="all,delete", backref="place")
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []
    @getter
    def reviews(self):
        """ filestorage relationship """
        from models import storage
        reviews = storage.all(Review)
        list = []
        for value in reviews.values():
            if value.place_id == self.id:
                list.append(value)
        return list
                
