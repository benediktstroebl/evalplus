```python
def numerical_letter_grade(grades):
    letter_grades = {
        4.0: 'A+',
        'A': 3.7,
        'A-': 3.3,
        'B+': 3.0,
        'B': 2.7,
        'B-': 2.3,
        'C+': 2.0,
        'C': 1.7,
        'C-': 1.3,
        'D+': 1.0,
        'D': 0.7,
        'D-': 0.0,
        'E': 0.0
    }
    result = []
    for grade in grades:
        for l, h in letter_grades.items():
            if grade >= h:
                result.append(l)
                break
    return result
```