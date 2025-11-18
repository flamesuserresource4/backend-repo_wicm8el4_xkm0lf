"""
Database Schemas for Kavarna Cacao CMS

Each Pydantic model represents a MongoDB collection. The collection name is the
lowercased class name. For example: MenuItem -> "menuitem".

Collections used:
- Category: Product categories like Coffee, Ice Cream, Desserts, Food, Drinks
- Product: Individual product entries (optional price)
- MenuItem: Items shown on the featured menu / price list
- Location: Cafe locations with address, hours, images, and coordinates
- GalleryImage: Lifestyle and product photography entries
- PartnerInquiry: Leads for franchise/partnership requests
"""

from pydantic import BaseModel, Field
from typing import Optional, List


class Category(BaseModel):
    name: str = Field(..., description="Category name e.g., Coffee")
    slug: str = Field(..., description="URL-friendly identifier")
    description: Optional[str] = Field(None, description="Short micro description")
    image: Optional[str] = Field(None, description="Cover image URL for the category")


class Product(BaseModel):
    name: str = Field(..., description="Product name")
    category: str = Field(..., description="Category slug this product belongs to")
    description: Optional[str] = Field(None, description="Short description")
    price: Optional[float] = Field(None, ge=0, description="Optional price")
    image: Optional[str] = Field(None, description="Image URL")


class MenuItem(BaseModel):
    name: str = Field(..., description="Menu item name")
    description: Optional[str] = Field(None, description="Short note or tasting notes")
    price: Optional[float] = Field(None, ge=0, description="Price amount")
    currency: str = Field("€", description="Currency symbol")
    category: Optional[str] = Field(None, description="Optional grouping, e.g., Coffee, Desserts")


class Location(BaseModel):
    name: str = Field(..., description="Location name")
    address: str = Field(..., description="Street and city")
    opening_hours: str = Field(..., description="Opening hours string")
    image: Optional[str] = Field(None, description="Image URL of the location")
    latitude: Optional[float] = Field(None, description="Latitude for map")
    longitude: Optional[float] = Field(None, description="Longitude for map")


class GalleryImage(BaseModel):
    title: Optional[str] = Field(None, description="Caption or title")
    image: str = Field(..., description="Image URL")
    category: Optional[str] = Field(None, description="Optional tag e.g., coffee, dessert, space")


class PartnerInquiry(BaseModel):
    name: str = Field(..., description="Contact name")
    email: str = Field(..., description="Contact email")
    message: Optional[str] = Field(None, description="Short message")
    location_interest: Optional[str] = Field(None, description="City or country of interest")
