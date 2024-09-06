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

The task is to create a function that converts a list of student GPAs to a list of letter grades based on a predefined grading table. The grading table consists of GPA ranges and corresponding letter grades. The function handles various GPA scenarios and returns the appropriate letter grades using a dictionary lookup and some basic rounding logic.

This Python function tackles the problem:
1. The function `numerical_letter_grade` takes a list of student GPAs as its input `grades`.
2. It utilizes a dictionary `letter_grades` that maps a variety of letter grades to a list of GPA ranges.
3. The function iterates through each GPA in the input list.
4. For each GPA, it checks the `letter_grades` dictionary to find the key that matches the student's GPA range, using the round function to round the GPA to the nearest percentile.
5. It then returns the corresponding letter grade for that GPA, taken from the dictionary's value list corresponding to that key.

The result is a list of letter grades appropriately assigned to the student GPAs based on the predefined grading table.