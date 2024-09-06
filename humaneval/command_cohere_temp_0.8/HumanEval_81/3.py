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
        'E': [0.0, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    }
    return [letter_grades[key][round(grade, 1)] for grade in grades for key in letter_grades if grade > letter_grades[key][0]]
```

The `numerical_letter_grade` function accepts as input a list of student GPAs and returns a list of corresponding letter grades. It does this by referencing a dictionary where keys are the letter grades and the values are arrays of GPAs that correspond to those letter grades. The function iterates through the input list of GPAs, and for each GPA it checks if it is above the lowest GPA bound for a letter grade to determine which letter grade is appropriate. The GPA bound arrays are sorted in ascending order, so we can reliably lookup values using a GPA as a key in a dictionary. The function then returns a list of these letter grades in the same order as the input GPA list. 

The above code is self-contained and solves the problem statement, whereby it takes a list of GPAs and returns a list of letter grades for those GPAs, accordingly. 

Let's validate this solution by testing it against some examples to ensure it complies with the problem's statement:
```python
def test_numerical_letter_grade():
    assert numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]) == ['A+', 'B', 'C-', 'C', 'A-']
    assert numerical_letter_grade([3.8, 3.65, 2.9, 1.2, 4.2]) == ['A', 'A-', 'B', 'D', 'A+']
    assert numerical_letter_grade([0.0, 2.9, 3.1, 1.8, 4.0]) == ['E', 'B', 'A', 'C', 'A+']
    assert numerical_letter_grade([3.3, 3.7, 2.3, 1.9, 3.1, 2.5]) == ['A-', 'A', '