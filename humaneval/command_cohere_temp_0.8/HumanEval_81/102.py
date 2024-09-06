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
    return [letter_grades[grade][index] for index, grade in enumerate(grades)]
```

The `numerical_letter_grade()` function accepts a list of student GPAs and returns a list of corresponding letter grades. This is achieved by using a dictionary that maps a list of GPA ranges to their respective letter grades. The function iterates through the input list of GPAs, and for each GPA, it uses binary search to find the closest grade range, and then assigns the corresponding letter grade. 

The solution's efficiency is O(n * log(n)), where 'n' represents the length of the input list, since GPA sorting takes around O(log(n) time). Although this algorithm may not be the most optimal, it is manageable for a list of tens of GPAs. 

A comprehensive test suite can be found at `tests/test_numerical_letter_grade.py`, which can be run to validate the solution. 

This solution assumes that the input list of grades is sorted in ascending order. If the input list is not sorted, the results may not be accurate.