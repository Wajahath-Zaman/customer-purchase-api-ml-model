from pydantic import BaseModel, Field

class Customer(BaseModel):
    age: int = Field(..., ge=18, le=100)
    income:float = Field(..., ge=0)
    previous_purchases:int = Field(..., ge=0)
    city:str
    device:str


class PredictResponse(BaseModel):
    prediction: int
    purchase_probability: float

