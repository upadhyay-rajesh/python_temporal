from fastapi import APIRouter, Depends
from app.services.student_service import StudentService
from fastapi import HTTPException
from app.schemas.student_schema import *
from app.config.database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/student",
    tags=["student"]
)

@router.get("/")
def get_students(db:Session = Depends(get_db)):
    return StudentService.get_all_students(db)

@router.get("/{student_id}")
def get_student(student_id: int, db:Session = Depends(get_db)):
    student = StudentService.get_student_by_id(student_id,db)

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@router.post("/")
def create_student(
    student: StudentCreate,
    db: Session = Depends(get_db)
):
    return StudentService.create_student(
        db,
        student
    )

@router.put("/{student_id}")
def update_student(student_id: int, student: StudentCreate,db:Session = Depends(get_db)):
    updated_student = StudentService.update_student(student_id, student,db)

    if not updated_student:
        raise HTTPException(status_code=404, detail="Student not found")
    return updated_student

@router.delete("/{student_id}")
def delete_student(student_id: int,db:Session = Depends(get_db)):
    success = StudentService.delete_student(db,student_id)

    if not success:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"detail": "Student deleted successfully"}