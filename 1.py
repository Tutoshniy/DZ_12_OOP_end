class NameValidator:
    def __get__(self, instance, owner):
        return instance._name

    def __set__(self, instance, value):
        if not value.isalpha():
            raise ValueError("Имя должно содержать только буквы")
        if not value.istitle():
            raise ValueError("Имя должно начинаться только с заглавной буквы")
        instance._name = value


class Student:
    name = NameValidator()

    def __init__(self, subjects_file):
        self.subjects = []
        with open(subjects_file, 'r') as f:
            for line in f:
                subject = line.strip()
                if subject:
                    self.subjects.append(subject)
        self.grades = {subject: [] for subject in self.subjects}
        self.tests = {subject: [] for subject in self.subjects}

    def add_grade(self, subject, grade):
        if subject not in self.subjects:
            raise ValueError(f"{subject} недопустимой значение для этого студента")
        if grade < 2 or grade > 5:
            raise ValueError("Оценка должна быть между 2 и 5")
        self.grades[subject].append(grade)

    def add_test_result(self, subject, result):
        if subject not in self.subjects:
            raise ValueError(f"{subject} недопустимой значение для этого студента")
        if result < 0 or result > 100:
            raise ValueError("Результат теста должен быть между 0 и 100")
        self.tests[subject].append(result)

    def average_test_result(self, subject):
        if subject not in self.subjects:
            raise ValueError(f"{subject} недопустимой значение для этого студента")
        if not self.tests[subject]:
            return 0
        return sum(self.tests[subject]) / len(self.tests[subject])

    def average_grade(self):
        total_grades = []
        for subject in self.subjects:
            total_grades.extend(self.grades[subject])
        if not total_grades:
            return 0
        return sum(total_grades) / len(total_grades)

