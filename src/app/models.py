from typing import Optional
from pydantic import BaseModel

class ItemPayload(BaseModel):
    item_id: Optional[int]
    item_name: str
    quantity: int
    test: str
    keyword: str
    nothing: str
    num: int
    
    
class ItemTestModel(BaseModel):
    keyword: str