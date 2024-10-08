python
def numerical_letter_grade(grades):
    grade_scale = {
        4.0: 'A+',
        3.7: 'A',
        3.3: 'A-',
        3.0: 'B+',
        2.7: 'B',
        2.3: 'B-',
        2.0: 'C+',
        1.7: 'C',
        1.3: 'C-',
        1.0: 'D+',
        0.7: 'D',
        0.0: 'D-',
        -1: 'E'
    }

    letter_grades = []
    for grade in grades:
        for gpa, letter_grade in grade_scale.items():
            if grade >= gpa:
                letter_grades.append(letter_grade)
                break
        else:
            letter_grades.append(grade_scale[-1])

    return letter_grades
