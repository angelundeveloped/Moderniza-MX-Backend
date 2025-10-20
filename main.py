"""Moderniza MX Backend Application."""

from turtle import title
from fastapi import FastAPI

moderniza_mx_app = FastAPI(
    title="Moderniza MX Backend",
    description="Backend application for Moderniza MX platform.",
    version="0.0.0",
)

@moderniza_mx_app.get("/")
async def read_root():
    return {"message": "Welcome to the Moderniza MX Backend!"}
