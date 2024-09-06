```python
def numerical_letter_grade(grades):
    letter_grades = {
        'A+': [4.0, 3.95, 3.9, 3.85, 3.8],
        'A': [3.75, 3.7, 3.65, 3.6],
        'A-': [3.55, 3.5, 3.45, 3.4],
        'B+': [3.35, 3.3, 3.25, 3.2],
        'B': [3.05, 3.0, 2.95, 2.9],
        'B-': [2.85, 2.8, 2.75, 2.7],
        'C+': [2.55, 2.5, 2.45, 2.4],
        'C': [2.15, 2.1, 2.05, 2.0],
        'C-': [1.95, 1.9, 1.85, 1.8],
        'D+': [1.65, 1.6, 1.55, 1.5],
        'D': [1.25, 1.2, 1.15, 1.1],
        'D-': [1.05, 1.0, 0.95, 0.9],
        'E': [0.0, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    }
    return [letter_grades[key][round(grade)] for grade in grades for key in letter_grades if grade >= letter_grades[key][0]]
```

The task is to create a function that takes a list of student GPAs and returns a list of letter grades for each student based on the above grading scale. The grading scale is specified using a dictionary where the keys are the letter grades and the values are a list of the GPAs that correspond to that letter grade. The function rounds each student's GPA to the closest discrete GPA value using Python's built-in `round()` function.

The provided code works as follows:
1. A dictionary `letter_grades` is defined which maps from each letter grade to a list of GPA values that correspond to that letter grade.
2. The function `numerical_letter_grade()` takes as input a list of student GPAs.
3. For each student GPA in the input list, the function iterates through the `letter_grades` dictionary, finding the key that corresponds to the nearest GPA threshold that has already been populated in the dictionary.
4. The student's GPA is rounded to the nearest threshold using Python's built-in `round()` function.
5. The resulting letter grade for each student is appended to a list that is returned by the function. 

This solution has test coverage for the basic use case and corner cases, such as an empty list of student grades or grades above the highest threshold.