from datetime import datetime

class Student:
    def __init__(self, name):
        self.name = name
        self._enrollments = []
        self._grades = {}  # Key: Enrollment, Value: numeric grade

    def enroll(self, course):
        if isinstance(course, Course):
            enrollment = Enrollment(self, course)
            self._enrollments.append(enrollment)
            course.add_enrollment(enrollment)
        else:
            raise TypeError("course must be an instance of Course")

    def get_enrollments(self):
        return self._enrollments.copy()

    def course_count(self):
        return len(self._enrollments)

    def set_grade(self, enrollment, grade):
        if not isinstance(enrollment, Enrollment):
            raise TypeError("Must pass a valid Enrollment")
        self._grades[enrollment] = grade

    def average_grade(self):
        if not self._grades:
            return 0
        return sum(self._grades.values()) / len(self._grades)


class Course:
    def __init__(self, title):
        self.title = title
        self._enrollments = []

    def add_enrollment(self, enrollment):
        if isinstance(enrollment, Enrollment):
            self._enrollments.append(enrollment)
        else:
            raise TypeError("enrollment must be an instance of Enrollment")

    def get_enrollments(self):
        return self._enrollments.copy()

    def student_count(self):
        return len(self._enrollments)


class Enrollment:
    all = []

    def __init__(self, student, course):
        if isinstance(student, Student) and isinstance(course, Course):
            self.student = student
            self.course = course
            self._enrollment_date = datetime.now()
            type(self).all.append(self)
        else:
            raise TypeError("Invalid types for student and/or course")

    def get_enrollment_date(self):
        return self._enrollment_date

    @classmethod
    def enrollments_per_day(cls):
        count_by_day = {}
        for enrollment in cls.all:
            date = enrollment.get_enrollment_date().date()
            count_by_day[date] = count_by_day.get(date, 0) + 1
        return count_by_day
