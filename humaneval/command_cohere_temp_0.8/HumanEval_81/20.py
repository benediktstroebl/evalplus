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
    return [letter_grades[key][round(grade)] for grade in grades for key in letter_grades if grade in letter_grades[key]]
```

The task is to create a function that converts a list of numerical grades into a list of letter grades. This is achieved by mapping each grade to its corresponding letter grade using a predefined lookup table. The lookup table lists grade ranges in numerical order and the corresponding letter grades. The function iterates through each grade in the input list and uses the lookup table to find the corresponding letter grade. The output list contains the letter grades in the same order as the input list. A key aspect of this approach is the use of the `round()` function to determine the closest match in the lookup table, this is important because some grade ranges in the table are inclusive of their endpoints whereas others are not. And the `round()` function ensures we hit the correct endpoint. 

To test the function, we could simply check if it behaves as expected on a variety of input lists, see the example below:
```python
def test_numerical_letter_grade():
    assert numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]) == ['A+', 'B', 'C-', 'C', 'A-']
    assert numerical_letter_grade([3.8, 3.2, 2.3, 1.8, 4.2]) == ['A', 'A-', 'B', 'C', 'A+']
    assert numerical_letter_grade([0.0, 2.5, 2.8, 3.6, 3.0]) == ['E', 'C', 'B', 'A', 'A-']
test_numerical_letter_grade()
```

However, the above tests are rather simplistic, and do not consider edge cases and specific scenarios that a more robust function would have to deal with. Thus an improved test suite could be:
```python
def test_numerical_letter_grade():
    assert numerical_letter_grade([4.0, 3, 1.7, 2,