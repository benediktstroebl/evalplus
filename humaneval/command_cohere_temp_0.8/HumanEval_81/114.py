```python
def numerical_letter_grade(grades):
    letter_grades = {
        'A+': [4.0, 3.95, 3.9, 3.85, 3.8],
        'A': [3.75, 3.7, 3.65, 3.6],
        'A-': [3.55, 3.5, 3.45, 3.4],
        'B+': [3.35, 3.3, 3.25, 3.2],
        'B': [3.05, 3.0, 2.95, 2.9],
        'B-': [2.85, 2.8, 2.75, 2.7],
        'C+': [2.65, 2.6, 2.55, 2.5],
        'C': [2.35, 2.3, 2.25, 2.2],
        'C-': [2.05, 2.0, 1.95, 1.9],
        'D+': [1.65, 1.6, 1.55, 1.5],
        'D': [1.35, 1.3, 1.25, 1.2],
        'D-': [1.05, 1.0, 0.95, 0.9],
        'E': [0.0, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.75, 0.8, 0.85, 0.9]
    }
    return [letter_grades[key][round(grade)] for grade in grades for key in letter_grades if grade in letter_grades[key]]
```

The task is to create a function that converts a list of numerical grades into a list of letter grades. The input is a list of GPAs and the output is a list of letter grades corresponding to the numerical GPAs based on the given specification.

This Python script defines a function `numerical_letter_grade` that takes in a list of student GPAs and returns a list of letter grades for each student based on the given grading scheme. The script first defines a dictionary `letter_grades` that maps numerical ranges to letter grades. Then, the function iterates through each GPA in the input list and uses the `letter_grades` dictionary to find the appropriate letter grade for each GPA. Finally, the function returns a list of the calculated letter grades in the same order as the input GPAs. 

This approach has a threshold for each range as the basis for the mapping, which makes it a basic numerical analysis approach. With the help of the built-in Python `round()` function, it is easier to map the grades exactly to the schema.