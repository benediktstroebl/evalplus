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
    return [letter_grades.get(grade)[round(grades[i]-min(grade_grades[grade]))] for i, grade in enumerate(grades)]
```

The task is to create a function that converts a list of numerical grades into a list of letter grades. We create a dictionary that maps a list of GPA ranges to letter grades and then use it to translate the provided GPAs to their corresponding letter grades. To avoid issues with rounding, we round the GPA for each student up to the nearest hundredth and use that value to find the correct letter grade. As our dictionary doesn't map the exact GPA value of each student, we find the closest range using the `min()` function and subtract this value to get the correct letter grade. For example, if a student has a GPA of 3.7, the expression `min(grade_grades['A'])` returns 3.5, and subtracting this value gives us the correct range of 3.65-3.6 which maps to the letter grade 'A'.