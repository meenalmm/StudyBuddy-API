from fastapi import APIRouter

router = APIRouter()

@router.get("/users")
def get_users():
    return [{"name": "Alice"}, {"name": "Bob"}]