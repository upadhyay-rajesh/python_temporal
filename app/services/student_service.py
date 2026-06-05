from app.models.student_model import Student

class StudentService:

    @staticmethod
    def get_all_students(db):
        return db.query(Student).all()

    @staticmethod
    def get_student_by_id(student_id,db):
        return db.query(Student)\
                 .filter(Student.id == student_id)\
                 .first()

    @staticmethod
    def create_student(db, student_data):

        student = Student(
            name=student_data.name,
            age=student_data.age,
            email=student_data.email
        )

        db.add(student)
        db.commit()
        db.refresh(student)

        return student

    @staticmethod
    def update_student(
        
        student_id,
        student_data,
        db
    ):

        student = db.query(Student)\
                    .filter(Student.id == student_id)\
                    .first()

        if student:
            student.name = student_data.name
            student.age = student_data.age
            student.email = student_data.email

            db.commit()
            db.refresh(student)

        return student

    @staticmethod
    def delete_student(
        db,
        student_id
    ):

        student = db.query(Student)\
                    .filter(Student.id == student_id)\
                    .first()

        if student:
            db.delete(student)
            db.commit()

        return student