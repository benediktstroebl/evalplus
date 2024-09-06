```python
def numerical_letter_grade(grades):
    letter_grades = {
        'A+': [4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0],
        'A': [3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0],
        'A-': [3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0],
        'B+': [3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0,0],
        'B': [2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0, 0.0],
        'B-': [2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0, 0.0],
        'C+': [2.0, 1.7, 1.3, 1.0, 0.7, 0.0, 0.0],
        'C': [1.7, 1.3, 1.0, 0.7, 0.0, 0.0],
        'C-': [1.3, 1.0, 0.7, 0.0, 0.0],
        'D+': [1.0, 0.7, 0.0, 0.0],
        'D': [0.7, 0.0, 0.0],
        'D-': [0.0, 0.0],
        'E': [0.0]
    }
    return [letter_grades[letter][gpa] for letter, gpa in zip(letter_grades.keys(), grades)]
```

The approach here is to create a dictionary with the GPA thresholds as keys and the corresponding letter grades as values and then use basic python functionality to lookup the corresponding grade given a GPA. 

This approach does not require additional modules and is suitable for this particular problem. Note that, if you were to take a grading scale with more complexity (e.g., multiple thresholds for certain grades), a different approach may be required, such as using a database or overload functions. 

The tests for this problem will generally take the form of checking that the function returns the expected outputs for a given set of GPAs. For example:
```python
tests = {
    'grade_equation([4.0, 3, 1.7, 2, 3.5])': ['A+', 'B', 'C-', 'C', 'A-'],
    'grade_equation([3.8, 3.2, 1.8, 1.2, 3.7])': ['A', 'B', 'D', 'C', 'A-'],
    'grade_equation([2.2, 2.5, 2.8, 1.9, 2.1])': ['C+', 'B', 'B', 'C', 'C-'],
}

for test, expected in tests.items():
    assert numerical_letter_grade(eval(test)) == expected
```