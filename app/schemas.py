from pydantic import BaseModel, ConfigDict


class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    completed: bool = False


class TaskUpdate(BaseModel):
    title: str
    description: str | None = None
    completed: bool = False


class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None
    completed: bool
    created_at: object

    """class Config:
        from_attributes = True"""
    model_config = ConfigDict(from_attributes=True)