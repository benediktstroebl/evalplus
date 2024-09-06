```python
def numerical_letter_grade(grades):
    letter_grades = {
        'A+': [4.0, None, None, None, None],
        'A': [3.7, 3.3, None, None, None],
        'A-': [3.0, 3.7, 3.3, None, None],
        'B+': [2.7, 2.3, 3.0, None, None],
        'B': [2.3, 2.7, 2.3, 1.7, None],
        'B-': [2.0, 2.3, 2.7, 1.7, 1.3],
        'C+': [1.7, 1.3, 2.0, 1.3, None],
        'C': [1.3, 1.7, 1.3, 0.7, None],
        'C-': [1.0, 1.3, 1.7, 0.7, 0.3],
        'D+': [0.7, None, 1.0, 0.7, None],
        'D': [0.3, 0.7, None, 0.3, None],
        'D-': [0.0, 0.3, 0.7, 0.3, 0],
        'E': [None, None, None, None, 0.0]
    }
    return [letter_grades[letter][gpa > threshold] for letter, threshold in letter_grades.items()]
```

The logic behind this approach is quite straightforward. We define a dictionary `letter_grades`, where each key is a letter grade and each value is a list of cut-off thresholds for the corresponding GPA. Then we use basic python comprehension to iterate over the dictionary and return the letter grades accordingly.

Note that the special None values in the letter_grades dictionary allow us to handle the less-than comparisons in a cleaner way, leaving us with no conditional statements (such as `if threshold_value:`) in the code. Also, this approach is resilient to different GPA thresholds as well as any additional letter grades that might be added in the grading scheme.