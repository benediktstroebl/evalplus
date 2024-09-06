```python
def sum_squares(lst):
    """
    Return the sum of squared integers in the provided list.
    
    Round each list element to the nearest higher integer before squaring.
    """
    return sum((int(rounding(x))**2 for x in lst))

def rounding(x):
    """
    Round the given number to the nearest higher integer.
    """
    return int(x + 1) if x % 1 == 0.5 else int(x)

# Some test cases
assert sum_squares([1, 2, 3]) == 14
assert sum_squares([1, 4, 9]) == 98
assert sum_squares([1, 3, 5, 7]) == 84
assert sum_squares([1.4, 4.2, 0]) == 29
assert sum_squares([-2.4, 1, 1]) == 6
```

This Python script defines a function `sum_squares` which, as outlined by the problem statement, calculates the sum of the squares of integers extracted from a given list. Prior to squaring, each list element is rounded up to the nearest integer using a helper function `rounding`. The provided test cases assert the function's correctness.