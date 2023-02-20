class Student:
    all_students = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.all_students.append(self)

    def evaluation_of_teachers(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) \
                and course in (self.courses_in_progress or self.finished_courses) \
                and course in lecturer.courses_attached \
                and grade in range(1, 11):
            if course in lecturer.grades_of_students:
                lecturer.grades_of_students[course] += [grade]
            else:
                lecturer.grades_of_students[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}' \
              f'\nСредняя оценка за домашнее задания: ' \
              f'{self.avg_student_grade()}' \
              f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}' \
              f'\nЗавершенные курсы: {", ".join(self.finished_courses)}'

        return res

    def avg_student_grade(self):
        count = 0
        res = 0
        print(self.grades)
        for i in self.grades.values():
            res += sum(i)
            count += len(i)

        return round(res / count, 2)

    def __lt__(self, other):
        x = self
        y = other

        if isinstance(other, Student):
            if x.avg_student_grade() < y.avg_student_grade():
                x, y = y, x

            print(
                f'У {x.name}({x.avg_student_grade()}) больше средняя оценка, чем у {y.name}({y.avg_student_grade()})')
            return


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    all_lecturers = []

    def __init__(self, name, surname):
        self.all_lecturers.append(self)
        super().__init__(name, surname)
        self.grades_of_students = {}

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}' \
              f'\nСредняя оценка за лекции: ' \
              f'{self.avg_lectors_grade()}'

        return res

    def avg_lectors_grade(self):
        count = 0
        res = 0
        print(self.grades_of_students)
        for i in self.grades_of_students.values():
            res += sum(i)
            count += len(i)

        return res / count

    def __lt__(self, other):
        x = self
        y = other

        if isinstance(other, Lecturer):
            if x.avg_lectors_grade() < y.avg_lectors_grade():
                x, y = y, x

            print(f'У {x.name}({x.avg_lectors_grade()}) больше средняя оценка, чем у {y.name}({y.avg_lectors_grade()})')
        else:
            raise AttributeError('Такого лектора не существует')


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        """" """
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str___(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'

        return res


def avg_grades_students_on_course(course):
    res = 0
    count = 0
    for student in Student.all_students:
        for course_from_dict in student.grades:
            # print(course_from_dict)
            if course == course_from_dict:
                print(student.grades[course])
                res += sum(student.grades[course]) / len(student.grades[course])
                count += 1


def avg_grades_lectors_on_course(course):
    res = 0
    count = 0
    for lecturer in Lecturer.all_lecturers:
        for course_from_dict in lecturer.grades_of_students:
            if course == course_from_dict:
                print(lecturer.grades_of_students[course])
                res += sum(lecturer.grades_of_students[course]) / len(lecturer.grades_of_students[course])
                count += 1

    return round(res / count, 2)


if __name__ == '__main__':
    k = Student('Chinya', 'Gakhaev', 'male')
    z = Reviewer('Rinat', 'Asadov')
    p = Lecturer('Viktor', 'Batyrov')
    k.courses_in_progress += ['Python', 'Java']
    a = Student('Alex', 'Ananko', 'male')
    p.courses_attached += ['Python', 'Java']
    a.courses_in_progress += ['Python', 'Java']
    z.courses_attached += ['Java', 'Python']
    a.finished_courses += ['Git']
    r = Lecturer('Mergen', 'Modunkaev')
    r.courses_attached += ['Python', 'Java']

    z.rate_hw(a, 'Python', 10)
    z.rate_hw(k, 'Python', 1)
    z.rate_hw(k, 'Python', 7)
    z.rate_hw(k, 'Python', 8)
    z.rate_hw(a, 'Python', 3)
    z.rate_hw(a, 'Python', 2)
    z.rate_hw(a, 'Java', 10)
    a.evaluation_of_teachers(p, 'Python', 10)
    a.evaluation_of_teachers(p, 'Python', 7)
    a.evaluation_of_teachers(p, 'Python', 3)
    a.evaluation_of_teachers(p, 'Java', 6)

    a.evaluation_of_teachers(r, 'Python', 9)
    a.evaluation_of_teachers(r, 'Python', 3)
    a.evaluation_of_teachers(r, 'Python', 6)
    a.evaluation_of_teachers(r, 'Java', 2)
    a.evaluation_of_teachers(r, 'Java', 5)
    # print(r.avg_lectors_grade())
    # print(a.avg_student_grade())

    print(avg_grades_lectors_on_course('Python'))
    # m = Lecturer.all_lectors
    # print(*m)
    # # var = r > p
    # # print(p)
    # # print(a)
    # # print(p.__dict__)
    # # print(a.__dict__)
    # #
    # # print(Student.all_students)
    # print(avg_grades_students_on_course('Python'))
    # print(a.grades)
