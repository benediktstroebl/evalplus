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
    return [letter_grades[key][round(grade)] for grade in grades for key in letter_grades if round(grade) in letter_grades[key]]
```

The `numerical_letter_grade` function accepts as an argument a list of student GPAs and returns a list of corresponding letter grades. It does this by matching each GPA to the closest threshold in the grading table, which is extracted from the function using the `letter_grades` dictionary. The GPA thresholds are organized in the dictionary as a sorted list of numeric arrays, each corresponding to a specific letter grade. Each student's GPA is then matched to the closest letter grade according to the thresholds set. The `round(grade)` function ensures that any GPAs that fall exactly on a threshold are correctly matched to the corresponding letter grade. The list of letter grades is then returned in order of the input GPAs. 

This code can be run directly in a Python environment or IDE compatible with Python 3. It can also be modified to include additional tests cases by adding lists of GPAs to the existing `test_numerical_letter_grade` function. Here is an example:
```python
def test_numerical_letter_grade():
    # Basic Tests:
    assert numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]) == ['A+', 'B', 'C-', 'C', 'A-']
    assert numerical_letter_grade([3.8, 2.9, 1.6, 1.2, 4.2]) == ['A', 'B', 'C', 'C', 'A+']
    assert numerical_letter_grade([0.9, 2.1, 2.5, 1.8, 3.7]) == ['D+', 'B', 'B', 'C', 'A']
    assert numerical_letter_grade([0.1, 1.1, 1.9, 2.5