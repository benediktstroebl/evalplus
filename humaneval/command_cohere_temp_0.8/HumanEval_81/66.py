```python
def numerical_letter_grade(grades):
    letter_grades = {
        'A+': [4.0, 3.95, 3.9, 3.85, 3.8],
        'A': [3.75, 3.7, 3.65, 3.6],
        'A-': [3.55, 3.5, 3.45, 3.4],
        'B+': [3.35, 3.3, 3.2, 3.15, 3.0],
        'B': [2.75, 2.7, 2.65, 2.6],
        'B-': [2.45, 2.4, 2.35, 2.3],
        'C+': [2.0, 1.95, 1.9, 1.85, 1.8],
        'C': [1.65, 1.6, 1.55, 1.5],
        'C-': [1.45, 1.4, 1.35, 1.3],
        'D+': [1.0, 0.95, 0.9, 0.85, 0.8],
        'D': [0.65, 0.6, 0.55, 0.5],
        'D-': [0.45, 0.4, 0.35, 0.3],
        'E': [0.0, 0.0]
    }
    return [letter_grades[grade_letter][round(grade)-1] for grade, grade_letter in zip(grades, letter_grades)]
```

The logic behind the grading system is to have a predefined list of GPAs for each letter grade, and a GPA threshold for each letter grade. The function uses an elegant and efficient approach using dictionaries and lists to map the GPA values to the corresponding letter grades. An example of use can be: `grade_equation([4.0, 3, 1.7, 2, 3.5]) ==> ['A+', 'B', 'C-', 'C', 'A-']`.