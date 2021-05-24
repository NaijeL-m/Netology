f=0
prepody = []
study = []


def mentor_chart():
    chart = {}
    print('Рейтинг преподавателей')
    for person in prepody:
        summ = 0
        count = 0
        for k, v in person.grade_l.items():
            summ += sum(v)
            count += len(v)
        if count == 0:
            count = 1
        chart[summ / count] = person.name + ' ' + person.surname
    chart2 = sorted(chart)
    for i in chart2:
        print(chart[i], ' ', i)


def student_chart():
    chart = {}
    print('Рейтинг студентов')
    for person in study:
        summ = 0
        count = 0
        for k, v in person.grades.items():
            summ += sum(v)
            count += len(v)
        if count == 0:
            count = 1
        chart[summ / count] = person.name + ' ' + person.surname
    chart2 = sorted(chart)
    for i in chart2:
        print(chart[i], ' ', i)


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        study.append(self)

    def __str__(self):
        summ = 0
        count = 0
        for k, v in self.grades.items():
            summ += sum(v)
            count += len(v)
        if count > 0:
            sredn = summ / count
        else:
            sredn = 0
        progKursi = ''
        for i in self.courses_in_progress:
            progKursi += i + ' '
        zakKursi = ''
        for i in self.finished_courses:
            zakKursi += i + ' '
        im = 'Имя :' + self.name
        fam = 'Фамилия: ' + self.surname
        srznach = 'Средняя оценка за домашние задания: ' + str(sredn)
        kurs = 'Курсы в процессе изучения: ' + progKursi
        zKurs = 'Завершенные курсы: ' + zakKursi
        return im + '\n' + fam + '\n' + srznach + '\n' + kurs + '\n' + zKurs

    def rate_lection(self, lecturer, course, grade_l):
        if isinstance(lecturer,
                      Lekturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grade_l:
                lecturer.grade_l[course].append(grade_l)
            else:
                lecturer.grade_l[course] = [grade_l]


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return 'Имя: ' + self.name + '\n' + 'Фамилия: ' + self.surname


class Lekturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grade_l = {}
        prepody.append(self)

    def __str__(self):
        summ = 0
        count = 0
        for k, v in self.grade_l.items():
            summ += sum(v)
            count += len(v)
        return 'Имя: ' + self.name + '\n' + 'Фамилия: ' + self.surname + '\n' + 'Средний балл за лекции: ' + str(
            summ / count)


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


best_student = Student('Ruoy', 'Eman', 'malchik')
best_student.courses_in_progress += ['Python']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached.append('Python')

some_lector = Lekturer('Iosif', 'Lazar')
some_lector.courses_attached.append('Python')
some_lector.courses_attached.append('HTML')
some_lector.courses_attached.append('C#')
s_lector = Lekturer('Vasya', 'Lenon')
s_lector.courses_attached.append('Python')
s_lector.courses_attached.append('HTML')
s_lector.courses_attached.append('C#')

some_student = Student('Ivanka', 'Clever', 'devochka')
some_student.finished_courses.append('Python')
some_student.courses_in_progress.append('HTML')
some_student.courses_in_progress.append('C#')

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
best_student.rate_lection(some_lector, 'Python', 6)
best_student.rate_lection(some_lector, 'Python', 8)
best_student.rate_lection(some_lector, 'Python', 10)
best_student.rate_lection(s_lector, 'Python', 5)
best_student.rate_lection(s_lector, 'Python', 7)
best_student.rate_lection(s_lector, 'Python', 9)

print(best_student.grades)
print(some_lector.grade_l)
print(some_lector)
print(s_lector)
print(cool_mentor)
print(some_student)
print(prepody)
mentor_chart()
student_chart()