from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Text, Boolean, ForeignKey, DateTime, func
from datetime import datetime

class Base(DeclarativeBase):
    id:Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

class CompanyType(Base):
    __tablename__ = "company_type"
    name: Mapped[str]
    # We could use backref instead of back_populates to skip the relationship() in the other class
    companies: Mapped[list["Company"]] = relationship("Company", back_populates="company_type")
    
    def __repr__(self):
        return f"<CompanyType={self.name}>"

class Company(Base):
    __tablename__ = "companies"
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    postal_code: Mapped[str] 
    email: Mapped[str] = mapped_column(String(1000))
    description: Mapped[str] = mapped_column(Text())
    analytics_module: Mapped[bool] = mapped_column(nullable=True)
    website: Mapped[str] = mapped_column(String(100), nullable=True)
    company_type: Mapped[CompanyType] = relationship("CompanyType", back_populates="companies")
    company_type_id: Mapped[int] = mapped_column(ForeignKey("company_type.id",  ondelete="SET NULL"), nullable=True)

    def __repr__(self):
        return f"<Company={self.name}>"
