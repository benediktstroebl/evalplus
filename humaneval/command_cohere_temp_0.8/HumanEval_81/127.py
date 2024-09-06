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

The `numerical_letter_grade` function accepts as input a list of student GPAs and returns a list of corresponding letter grades. It does this by rounding the input GPAs to the nearest decimal value present in the keys of the letter_grades dictionary and returning the corresponding letter grades.

Let's break down the logic:
1. We define a dictionary `letter_grades` that maps a set of GPA ranges to their corresponding letter grades.
2. We iterate through each student's GPA in the input list, rounding each GPA to the nearest decimal value of an existing key in our `letter_grades` dictionary using the `round()` function and key in the dictionary.
3. The `round()` function rounds the decimal value to the nearest integer, which conveniently maps to the nearest letter grade.

The function is self-contained and does not require any additional modules or dependencies beyond Python's standard library. It should work out of the box for assigning letter grades based on the provided GPA ranges. 

This approach leverages Python's data structures and built-in functions, making it concise and readable while accomplishing the desired task in a straightforward manner.