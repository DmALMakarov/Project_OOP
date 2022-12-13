class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.courses_in_progress = []
        self.finished_courses = []
        self.grades = {} 

    #Выставляем оценку лектору за лекцию
    def grade(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
   
    #Средняя оценка за предмет
    def average_rating(self):
        if not self.grades:
            return 0
        grades_course = []
        for new_grades in self.grades.values():
            grades_course.extend(new_grades)
        return round(sum(grades_course) / len(grades_course), 2)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n' \
        f'Средняя оценка за домашние задания: {self.average_rating()}\n' \
        f'Курсы в процессе обучения: {self.courses_in_progress}\n' \
        f'Завершенные курсы: {self.finished_courses}'
    
    def __le__(self, other):
        if not isinstance(other, Student):
            return 'Not list'
        return self.average_rating() > other.average_rating()

    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Not list'
        return self.average_rating() < other.average_rating()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return 'Not list'
        return self.average_rating() == other.average_rating()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {} 

    #Средняя оценка за лекцию
    def average_rating(self):
        if not self.grades:
            return 0
        grades_course = []
        for new_grades in self.grades.values():
           grades_course.extend(new_grades)
        return round(sum(grades_course) / len(grades_course), 2)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating()}'

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            return 'Not list'
        return self.average_rating() > other.average_rating()

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Not list'
        return self.average_rating() < other.average_rating()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return 'Not list'
        return self.average_rating() == other.average_rating()

class Reviewer (Mentor):
    def rate(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'
 

best_student_one = Student('Алексей', 'Пупкин', 'М')
best_student_two = Student('Алиса', 'Чудесная', 'Ж')

best_student_one.courses_in_progress += ['Введение в программирование']
best_student_one.courses_in_progress += ['Git']
best_student_one.finished_courses += ['Python']

best_student_two.courses_in_progress += ['Git']
best_student_two.courses_in_progress += ['Python']
best_student_two.finished_courses = ['Введение в программирование']

cool_mentor_one = Reviewer('Илон', 'Маск')
cool_mentor_two = Reviewer('Джон', 'Маккарти')
cool_mentor_one.courses_attached += ['Python']
cool_mentor_one.courses_attached += ['Введение в программирование']
cool_mentor_two.courses_attached += ['Git']
cool_mentor_two.courses_attached += ['Python']
cool_mentor_two.courses_attached += ['Введение в программирование']

cool_mentor_one.rate(best_student_one, 'Введение в программирование', 10)
cool_mentor_one.rate(best_student_one, 'Введение в программирование', 9)
cool_mentor_one.rate(best_student_one, 'Введение в программирование', 8)
cool_mentor_one.rate(best_student_one, 'Git', 10)
cool_mentor_one.rate(best_student_one, 'Git', 8)
cool_mentor_one.rate(best_student_one, 'Git', 6)
cool_mentor_two.rate(best_student_two, 'Python', 8)
cool_mentor_two.rate(best_student_two, 'Python', 7)
cool_mentor_two.rate(best_student_two, 'Python', 9)
cool_mentor_two.rate(best_student_two, 'Git', 8)
cool_mentor_two.rate(best_student_two, 'Git', 7)
cool_mentor_two.rate(best_student_two, 'Git', 6)

cool_lecturer_one = Lecturer('Бил', 'Гейтс')
cool_lecturer_two = Lecturer('Стив', 'Джобс')
cool_lecturer_one.courses_attached += ['Python']
cool_lecturer_one.courses_attached += ['Git']
cool_lecturer_two.courses_attached += ['Git']
cool_lecturer_two.courses_attached += ['Введение в программирование']

best_student_one.grade(cool_lecturer_two, 'Введение в программирование', 10)
best_student_one.grade(cool_lecturer_one, 'Введение в программирование', 10)
best_student_one.grade(cool_lecturer_one, 'Введение в программирование', 9)
best_student_one.grade(cool_lecturer_two, 'Git', 6)
best_student_one.grade(cool_lecturer_one, 'Git', 9)
best_student_one.grade(cool_lecturer_one, 'Git', 8)
best_student_two.grade(cool_lecturer_one, 'Python', 9)
best_student_two.grade(cool_lecturer_two, 'Python', 9)
best_student_two.grade(cool_lecturer_two, 'Python', 7)
best_student_two.grade(cool_lecturer_two, 'Python', 7)
best_student_two.grade(cool_lecturer_two, 'Git', 8)
best_student_two.grade(cool_lecturer_one, 'Git', 7)
best_student_two.grade(cool_lecturer_two, 'Git', 9)


print(f'Студенты:\n{best_student_one.__str__()}')
print()
print(best_student_two.__str__())
print()
print(f'Лекторы:\n{cool_lecturer_one.__str__()}')
print()
print(cool_lecturer_two.__str__())
print()
print(f'Проверяющие эксперты:\n{cool_mentor_one.__str__()}')
print()
print(cool_mentor_two.__str__())
print()
all_students = [best_student_one, best_student_two]
all_lecturers = [cool_lecturer_one, cool_lecturer_two]
all_courses = input('Средняя оценка по курсу.\nВведите название курса: ')
 
def average_score_test(all_students, all_courses):  
    grades_list = [] 
    for student in all_students:       
        grades_list.extend(student.grades.get(all_courses, []))
    if not grades_list:
        return "По такому курсу ни у кого нет оценок"
    return round(sum(grades_list) / len(grades_list), 2)
def average_grade_lectures(all_lecturer, all_courses):
    return average_score_test(all_lecturer, all_courses)
print(f'Средняя оценка для всех студентов по курсу {all_courses}: {average_score_test(all_students, all_courses)}')
print(f'Средняя оценка для всех лекторов по курсу {all_courses}: {average_grade_lectures(all_lecturers, all_courses)}')


