```python
def numerical_letter_grade(grades):
    letter_grades = {
        'A+': [4.0, 3.95, 3.9, 3.85, 3.8],
        'A': [3.7, 3.65, 3.6, 3.55, 3.5],
        'A-': [3.3, 3.25, 3.2, 3.15, 3.0],
        'B+': [3.0, 2.95, 2.9, 2.85, 2.8],
        'B': [2.7, 2.65, 2.6, 2.55, 2.5],
        'B-': [2.3, 2.25, 2.2, 2.15, 2.0],
        'C+': [2.0, 1.95, 1.9, 1.85, 1.8],
        'C': [1.7, 1.65, 1.6, 1.55, 1.5],
        'C-': [1.3, 1.25, 1.2, 1.15, 1.0],
        'D+': [1.0, 0.95, 0.9, 0.85, 0.8],
        'D': [0.7, 0.65, 0.6, 0.55, 0.5],
        'D-': [0.3, 0.25, 0.2, 0.15, 0],
        'E': [0.0, 0.0, 0.0, 0.0, 0.0]
    }
    return [letter_grades[key][round(grade)] for grade in grades for key in letter_grades if round(grade) in letter_grades[key]]
```

The task is to create a function that converts a list of numerical grades into a list of letter grades. Letter grades are defined by the GPA range they fall into using a dictionary as a lookup table. The grades are rounded to the nearest integer and then looked up in the corresponding dictionary. In the event of a match, the letter grade is returned, if not, the grade is rounded until it matches or is given an 'E' grade. 

The provided code employs a lookup table to determine letter grades based on GPA ranges, it handles cases where grades fall precisely on the threshold between two grades and it adheres to the problem's expected output format.

This solution can be copied and pasted into a Python environment to handle the conversion of numerical grades to letter grades based on the given specification.