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
    return [letter_grades.get(letter)[gpa >= min(letter_grades[letter]) for letter, gpa in zip('ABCDE', grades)]
    
# Test Cases
assert numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]) == ['A+', 'B', 'C-', 'C', 'A-']
assert numerical_letter_grade([3.8, 3.2, 2.9, 1.6, 4.2]) == ['A', 'A-', 'B', 'D', 'A+']
assert numerical_letter_grade([0.0, 2.5, 2.8, 3.2, 3.7]) == ['E', 'C', 'B', 'A-', 'A']
```

The function `numerical_letter_grade()` takes a list of student GPAs as input and returns a list of letter grades for each student based on the grading scale provided. The function uses a dictionary called `letter_grades` to map ranges of GPAs to corresponding letter grades based on the given grading scale. The list comprehension unzips the GPA and letter grades, and then uses `get()` to retrieve the correct letter grade based on the GPA meets the specified threshold for each letter grade.