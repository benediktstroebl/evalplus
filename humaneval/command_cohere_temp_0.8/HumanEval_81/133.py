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
        'C': [2.05, 2.0, 1.95, 1.9],
        'C-': [1.85, 1.8, 1.75, 1.7],
        'D+': [1.55, 1.5, 1.45, 1.4],
        'D': [1.05, 1.0, 0.95, 0.9],
        'D-': [0.85, 0.8, 0.75, 0.7],
        'E': [0.0, 0.0, 0.0, 0.0]
    }
    return [letter_grades[letter][round(grade)] for grade, letter in zip(grades, 'ABCDE')]
```
#### Explanation
- The Python dictionary `letter_grades` maps a letter grade to a GPA range.
- The function `numerical_letter_grade` takes a list of student GPAs as input.
- We iterate through each student GPA, alphabetically sorting them while zipping them with the letters 'ABCDE'.
- We round each GPA using the `round()` function. This is important to ensure that fractions like 3.8 are rounded to 3.8, instead of 3.85.
- We then look up the rounded GPA on the letter grade range using `letter_grades` to determine the corresponding letter.
- Finally, we return a list of letter grades for each student in the input order.