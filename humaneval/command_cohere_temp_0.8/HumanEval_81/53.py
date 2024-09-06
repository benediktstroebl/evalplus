```python
def numerical_letter_grade(grades):
    letter_grades = {
        'A+': [4.0, 3.95, 3.9, 3.85, 3.8],
        'A': [3.75, 3.7, 3.65, 3.6],
        'A-': [3.55, 3.5, 3.45, 3.4],
        'B+': [3.35, 3.3, 3.2, 3.15, 3.0],
        'B': [2.85, 2.8, 2.75, 2.7],
        'B-': [2.55, 2.5, 2.45, 2.4],
        'C+': [2.15, 2.1, 2.05, 2.0],
        'C': [1.65, 1.6, 1.55, 1.5],
        'C-': [1.45, 1.4, 1.35, 1.3],
        'D+': [1.05, 1.0, 0.95, 0.9],
        'D': [0.65, 0.6, 0.55, 0.5],
        'D-': [0.45, 0.4, 0.35, 0.3],
        'E': [0.0, 0.0]
    }
    return [letter_grades.get(grade)[round(grades[idx]-min(grade_grades[grade]), 1)] for grade, grade_grades in letter_grades.items() for idx in range(len(grades))]
```

The task is to implement a function to convert a list of numerical grades into a list of letter grades. This is accomplished by using a dictionary to map numerical grade ranges to letters. The function `numerical_letter_grade` takes in a list of student grades and uses the above schema to convert them into their corresponding letter grades which are returned in a list. 

This solution assumes that the grades are already sorted in ascending order and does not utilize any built-in functions in Python related to sorting. Thus, it is not guaranteed that the resulting list of letter grades will be in order.