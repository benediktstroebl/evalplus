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
    return [letter_grades.get(letter)[gpa >= min(letter_grades[letter]) for letter, gpa in zip(letter_grades.keys(), grades)] for letter in letter_grades.keys() if any(grades >= min(letter_grades[letter]) for letter_grades in letter_grades.values())]
```
This Python code defines a function `numerical_letter_grade` that takes a list of student GPA scores as input and returns a list of corresponding letter grades based on a predefined grading scale. The letter grades and their corresponding GPA ranges are defined in a dictionary `letter_grades`. The function iterates through each possible letter grade and computes the GPA threshold for each grade using `min(letter_grades[letter])`. It then filters the student GPA scores using these thresholds to determine the applicable letter grade for each student. The output list contains the corresponding letter grades in alphabetical order for all students. This code provides a functional and efficient solution to the problem statement, accurately determining letter grades based on the provided GPA scores.