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
        'E': [0.0, 0.0, 0.0, 0.0]
    }
    return [letter_grades[letter][gpa >= threshold] for letter, threshold in letter_grades.items() for gpa in grades]
```

The task is to create a function that converts a list of numerical grades into a list of letter grades. This is achieved by using a dictionary that maps numerical grade ranges to letters and a list of thresholds. The function iterates through the keys of the dictionary, which are the letter grades, and for each, it applies the corresponding threshold to determine the applicable letters. The function then returns a list of these letters for the given GPA scores.

### Example Usage:
```python
grade_equation([4.0, 3, 1.7, 2, 3.5]) ==> ['A+', 'B', 'C-', 'C', 'A-']
```

This would be the expected output, as it is stated in the problem statement.