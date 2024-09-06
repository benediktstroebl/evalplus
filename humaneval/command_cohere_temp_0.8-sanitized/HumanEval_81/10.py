def numerical_letter_grade(grades):
    letter_grades = {
        'A+': [4.0, None, None, None, None],
        'A': [3.7, 3.3, None, None, None],
        'A-': [3.0, 3.7, 3.3, None, None],
        'B+': [2.7, 2.3, 3.0, None, None],
        'B': [2.3, 2.7, 2.3, None, None],
        'B-': [2.0, 2.3, 2.7, None, None],
        'C+': [1.7, 1.3, 2.0, None, None],
        'C': [1.3, 1.7, 1.3, None, None],
        'C-': [1.0, 1.3, 1.7, None, None],
        'D+': [0.7, None, 1.0, None, None],
        'D': [0.0, 0.7, 1.0, None, None],
        'D-': [None, None, 0.7, 0.0, None],
        'E': [None, None, None, 0.0, None]
    }
    return [letter_grades[letter][gpa >= threshold] for letter, threshold in letter_grades.items() for gpa in grades]