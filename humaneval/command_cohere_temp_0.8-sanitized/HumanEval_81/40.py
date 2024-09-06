def numerical_letter_grade(grades):
    letter_grades = {
        'A+': [4.0, None, None, None, None, None, None, None, None, None, None],
        'A': [3.7, 3.8, 3.9, None, None, None, None, None, None, None, None],
        'A-': [3.3, 3.4, 3.5, 3.6, None, None, None, None, None, None, None],
        'B+': [3.0, 3.1, 3.2, 3.3, 3.4, None, None, None, None, None, None],
        'B': [2.7, 2.8, 2.9, 3.0, 3.1, 3.2, None, None, None, None, None],
        'B-': [2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, None, None, None, None],
        'C+': [2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, None, None, None],
        'C': [1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, None, None],
        'C-': [1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, None],
        'D+': [1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 2.9, None],
        'D': [0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, None],
        'D-': [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, None],
        'E': [0.0, None, None, None, None, None, None, None, None, None, None]
    }
    return [letter_grades[letter][gpa] for letter, gpas in letter_grades.items() for gpa in grades]