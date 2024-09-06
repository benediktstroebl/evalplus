```python
def sum_squares(lst):
    """
    Return the sum of squared numbers in the given list,
    round each element in the list to the nearest larger integer first.
    """
    result = sum(x ** 2 for x in lst if isinstance(x, (int, float)) and x >= 0)
    return result
```

The function `sum_squares` takes a list of numbers as input and returns the sum of squared integers in the list. Before calculating the sum of squares, the function filters out non-integer and negative numbers from the list using a generator expression.

To achieve this, the function utilizes Python's `sum` function and a generator expression `(x ** 2 for x in lst if isinstance(x, (int, float)) and x >= 0)` to calculate the sum of squared elements in the list. The condition `isinstance(x, (int, float))` ensures that only numeric values are considered, and `x >= 0` filters out negative numbers.

Here is a test suite to ensure the function behaves correctly:
```python
def test_sum_squares():
    # Official Test Cases:
    assert sum_squares([1, 2, 3]) == 14
    assert sum_squares([1, 4, 9]) == 98
    assert sum_squares([1, 3, 5, 7]) == 84
    assert sum_squares([1.4, 4.2, 0]) == 29
    assert sum_squares([-2.4, 1, 1]) == 6

    # Edge Cases:
    assert sum_squares([1, 2, 3, 4]) == 14
    assert sum_squares([0, 0, 0, 0]) == 0
    assert sum_squares([-2.4, 1.4, 1.9, 4.2, -0.1]) == 29

    # Only Integers:
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 285
    assert sum_squares([0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0

    # Only Negative Numbers:
    assert sum_squares([-1, -2, -3, -4, -5]) == 106

    # Mix of Positive and Negative Numbers:
    assert sum_squares([1, -2, 3, -4, 5]) == 93
``` 

The test suite includes official test cases provided in the problem statement and additional edge cases to ensure the function behaves correctly for different scenarios.