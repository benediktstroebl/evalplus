def numerical_letter_grade(grades):
    letter_grades = {
        'A+': [4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0],
        'A': [3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0],
        'A-': [3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0],
        'B+': [3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0],
        'B': [2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0],
        'B-': [2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0],
        'C+': [2.0, 1.7, 1.3, 1.0, 0.7, 0.0],
        'C': [1.7, 1.3, 1.0, 0.7, 0.0],
        'C-': [1.3, 1.0, 0.7, 0.0],
        'D+': [1.0, 0.7, 0.0],
        'D': [0.7, 0.0],
        'D-': [0.0],
        'E': [0.0]
    }
    return [letter_grades.get(letter)[gpa >= min and gpa < max] for letter, (min, max) in letter_grades.items() for gpa in grades]