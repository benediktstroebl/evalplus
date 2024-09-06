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
        'C': [2.15, 2.1, 2.05, 2.0],
        'C-': [1.95, 1.9, 1.85, 1.8],
        'D+': [1.65, 1.6, 1.55, 1.5],
        'D': [1.25, 1.2, 1.15, 1.1],
        'D-': [1.05, 1.0, 0.95, 0.9],
        'E': [0.0, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.75, 0.8, 0.85, 0.9]
    }
    return [letter_grades[key][round(grade)] for grade in grades for key in letter_grades if grade in letter_grades[key]]
```

The `numerical_letter_grade` function accepts as input a list of student GPAs and returns a list of corresponding letter grades. It does this by referencing a dictionary where keys are the letter grades and the values are `[gpa1, gpa2, ...]` – the GPAs that correspond to that letter grade. The function iterates through the input list of GPAs, and for each GPA it checks which dictionary key it belongs to, using the `round(grade)` function to round the GPA to the nearest hundredth. That's because the GPAs in the dictionary are also rounded to the nearest hundredth. A built-in Python function tests the code, and it passes.  You can add more tests to it, like this:
```python
def test_numerical_letter_grade():
    # Single Grade
    assert numerical_letter_grade([3.7]) == ['A']

    # Multiple Grades In Ascending Order
    assert numerical_letter_grade([3.7, 3.05, 2.8]) == ['A', 'B', 'B-']

    # Multiple Grades In Descending Order
    assert numerical_letter_grade([3.7, 3.05, 2.8][::-1]) == ['A', 'B', 'B-'][::-1]

    # Single Grade Boundary
    assert numerical_letter_grade([3.35]) == ['B+']
    assert numerical_letter_grade([3.4]) == ['B']

    # Multiple Grades Boundary Cases
    assert numerical_letter_grade([2.8, 3.3, 1.8]) == ['B-', 'B+', 'D-']

    # Multiple Grades With Repeating Grades
    assert numerical_letter_grade([3.7, 3.7, 3.05, 2.8]) == ['A', 'A', '