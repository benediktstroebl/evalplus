def numerical_letter_grade(grades):
    letter_grades = {
        'A+': [4.0, None, None, None, None, None, None, None, None],
        'A': [3.7, 3.3, None, None, None, None, None, None, None],
        'A-': [3.3, None, None, None, None, None, None, None, None],
        'B+': [3.0, 2.7, None, None, None, None, None, None, None],
        'B': [2.7, 2.3, None, None, None, None, None, None, None],
        'B-': [2.3, None, None, None, None, None, None, None, None],
        'C+': [2.0, 1.7, 1.3, None, None, None, None, None, None],
        'C': [1.7, 1.3, None, None, None, None, None, None, None],
        'C-': [1.3, None, None, None, None, None, None, None, None],
        'D+': [1.0, 0.7, None, None, None, None, None, None, None],
        'D': [0.7, None, None, None, None, None, None, None, None],
        'D-': [0.3, 0.0, None, None, None, None, None, None, None],
        'E': [0.0, None, None, None, None, None, None, None, None]
    }
    letter_grades = {key: value for key, value in letter_grades.items() if value is not None}
    return [letter_grades.get(max(letter_grades, key=lambda x: letter_grades[x])) for grade in grades]