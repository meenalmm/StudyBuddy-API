from fastapi import APIRouter

router = APIRouter()

@router.get("/groups")
def get_groups():
    return [{"name": "Study Group 1"}, 
            {"name": "Study Group 2"}]