from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Text, Boolean, ForeignKey, DateTime, func
from datetime import datetime

class Base(DeclarativeBase):
    id:Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

class Company(Base):
    __tablename__ = "companies"
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    postal_code: Mapped[str] 
    email: Mapped[str] = mapped_column(String(1000))
    description: Mapped[str] = mapped_column(Text())
    analytics_module: Mapped[bool] = mapped_column(nullable=True)

    def __repr__(self):
        return f"<Company={self.name}>"