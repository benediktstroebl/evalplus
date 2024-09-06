def numerical_letter_grade(grades):
    letter_grades = {
        'A+': [4.0, 3.95, 3.9, 3.85, 3.8],
        'A': [3.75, 3.7, 3.65, 3.6],
        'A-': [3.55, 3.5, 3.45, 3.4],
        'B+': [3.35, 3.3, 3.2, 3.15, 3.0],
        'B': [2.75, 2.7, 2.65, 2.6],
        'B-': [2.45, 2.4, 2.35, 2.3],
        'C+': [2.05, 2.0, 1.95, 1.9],
        'C': [1.65, 1.6, 1.55, 1.5],
        'C-': [1.25, 1.2, 1.15, 1.0],
        'D+': [0.75, 0.7, 0.65, 0],
        'D': [0.45, 0.4, 0.35, 0],
        'D-': [0.05, 0.0, 0.0],
        'E': [0.0]
    }
    return [letter_grades[letter][gpa <= max(letter_grades[letter])] for letter, letter_grade in letter_grades.items() for gpa in grades for letter_grade in letter_grade]