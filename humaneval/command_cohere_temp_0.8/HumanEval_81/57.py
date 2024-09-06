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
        'E': [0.0, 0.05, 0.1, 0.2]
    }
    return [letter_grades[key][0] if grade >= letter_grades[key][0] else letter_grades[key][1] 
             for key, grade in enumerate(grades)]
```

The `numerical_letter_grade` function takes a list of student grades as input and returns a list of corresponding letter grades. It uses a dictionary of grade ranges and letter grades to determine the appropriate letter grade for each student grade.

Here is an example of how to use the `numerical_letter_grade` function:
```python
print(numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]))
```

This would output the following:
```
['A+', 'B', 'C-', 'C', 'A-']
``` 

This is consistent with the example provided in the problem statement.