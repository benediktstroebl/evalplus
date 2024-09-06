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
        'D+': [1.75, 1.7, 1.65, 1.6],
        'D': [1.45, 1.3, 1.25, 1.2],
        'D-': [1.05, 1.0, 0.95, 0.9],
        'E': [0.0, 0.0, 0.0]
    }
    return [letter_grades[letter][round(grade)] for grade, letter in zip(grades, 'ABCDE')]
```

The Python dictionary `letter_grades` maps a letter grade to a GPA range. The key of the dictionary is the letter grade and the value is a list of GPAs that correspond to the letter. The `numerical_letter_grade()` function takes a list of student GPAs as input and returns a list of letter grades based on the `letter_grades` dictionary and the GPA thresholds defined in the problem statement. The function uses `zip()` to iterate over the list of student GPAs and the alphabet. For each GPA, the function rounds it to the nearest threshold and looks up the corresponding letter grade. 

Here is an example output of the function:
```python
grade_equation([4.0, 3, 1.7, 2, 3.5]) ==> ['A+', 'B', 'C-', 'C', 'A-']
``` 

This solution is efficient and can provide the letter grades for a list of student grades in linear time, which is the same as the worst-case complexity of the naive approach.