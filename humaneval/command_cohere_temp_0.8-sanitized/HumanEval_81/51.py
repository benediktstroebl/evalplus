def numerical_letter_grade(grades):
    letter_grades = {
        'A+': [4.0, None, None, None, None, None, None, None, None],
        'A': [3.7, 3.3, None, None, None, None, None, None, None],
        'A-': [3.3, None, None, None, None, None, None, None, None],
        'B+': [3.0, 2.7, None, None, None, None, None, None, None],
        'B': [2.3, 2.0, 1.7, None, None, None, None, None, None],
        'B-': [2.0, 1.7, 1.3, None, None, None, None, None, None],
        'C+': [1.7, 1.3, 1.0, 0.7, None, None, None, None, None],
        'C': [1.3, 1.0, 0.7, 0.3, None, None, None, None, None],
        'C-': [1.0, 0.7, 0.3, 0.0, None, None, None, None, None],
        'D+': [0.7, 0.3, 0.0, None, None, None, None, None, None],
        'D': [0.3, 0.0, None, None, None, None, None, None, None],
        'D-': [0.0, None, None, None, None, None, None, None, None],
        'E': [None, None, None, None, 0.0, None, None, None, None]
    }
    return [letter_grades[grade][idx] for grade in grades for idx in range(len(grades))]