```python
def numerical_letter_grade(grades):
    letter_grades = {
        'A+': [4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0],
        'A': [3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0],
        'A-': [3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0],
        'B+': [3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0],
        'B': [2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0],
        'B-': [2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0],
        'C+': [2.0, 1.7, 1.3, 1.0, 0.7, 0.0],
        'C': [1.7, 1.3, 1.0, 0.7, 0.0],
        'C-': [1.3, 1.0, 0.7, 0.0],
        'D+': [1.0, 0.7, 0.0],
        'D': [0.7, 0.0],
        'D-': [0.0],
        'E': [0.0]
    }
    return [letter_grades.get(letter)[gpa <= max(letter_grades[letter])] for letter, letter_grade in letter_grades.items() for gpa, grade in zip(grades, letter_grade) if grade]
```

The `numerical_letter_grade` function accepts as input a list of student GPA scores and returns a list of corresponding letter grades based on the grading scheme outlined in the prompt. It uses a dictionary `letter_grades` to map letter grades to GPA ranges. Each GPA range is represented as an array where the upper bound is at the index 0 and lower bounds at the end. The function then iterates through the GPAs and their corresponding letter grades, comparing each GPA to the sorted GPA ranges for each letter grade. The resulting letter grades are returned as a list.