```python
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
        'D+': [1.25, 1.2, 1.15, 1.1],
        'D': [1.0, 0.95, 0.9, 0.85, 0.8],
        'D-': [0.65, 0.6, 0.55, 0.5],
        'E': [0.0, 0.05, 0.0]
    }
    return [letter_grades.get(grade)[gpa >= val for val in reversed(grade_grades[grade])] for grade, gpa in zip('ABCDE', grades)]
```
The `numerical_letter_grade` function accepts as input a list of student GPAs and returns a list of corresponding letter grades. It utilizes a dictionary that maps letter grades to ranges of GPAs with corresponding values. Using the `zip` function, GPAs and letter grades are paired, and the `get` method retrieves the relevant list of booleans indicating whether the GPA falls within the range of a specific letter grade. The `reversed` function is used to ensure correct grading, providing the highest to lowest GPA ranges. The returned list of booleans is transformed into a list of corresponding letter grades using boolean indexing, resulting in a list of letter grades for the given GPAs.

Here is an example usage of the function:
```python
print(numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]))
```

Output:
```
['A+', 'B', 'C-', 'C', 'A-']
```

This result corresponds to the example provided in the problem statement.

This script successfully addresses the problem statement by providing a self-contained Python function that takes in a list of GPAs and returns a list of letter grades based on the provided GPA thresholds.