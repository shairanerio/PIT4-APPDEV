from pydantic import BaseModel
from typing import Optional

class TodoBase(BaseModel):
    text: str
    completed: bool = False

class TodoCreate(TodoBase):
    pass

class TodoUpdate(BaseModel):
    text: Optional[str] = None
    completed: Optional[bool] = None

class Todo(TodoBase):
    id: int

    class Config:
        orm_mode = True
