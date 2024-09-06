def numerical_letter_grade(grades):
    letter_grades = {
        'A+': [4.0, 3.95, 3.9, 3.85, 3.8],
        'A': [3.75, 3.7, 3.65, 3.6],
        'A-': [3.55, 3.5, 3.45, 3.4],
        'B+': [3.25, 3.2, 3.15, 3.1],
        'B': [3.0, 2.95, 2.9, 2.85, 2.8],
        'B-': [2.75, 2.7, 2.65, 2.6],
        'C+': [2.4, 2.35, 2.3, 2.25, 2.2],
        'C': [2.0, 1.95, 1.9, 1.85, 1.8],
        'C-': [1.65, 1.6, 1.55, 1.5],
        'D+': [1.2, 1.15, 1.1, 1.05, 1.0],
        'D': [0.7, 0.65, 0.6, 0.55, 0.5],
        'D-': [0.4, 0.35, 0.3, 0.25, 0.2],
        'E': [0.0, 0.0]
    }
    return [letter_grades[key][round(grade)] for grade in grades for key in letter_grades if round(grade) in letter_grades[key]]