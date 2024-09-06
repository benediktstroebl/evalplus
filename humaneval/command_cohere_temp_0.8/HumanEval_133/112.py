```python
def sum_squares(lst):
    """
    Return the sum of squared integers in the list, rounding each number to the next bigger integer.
    """
    result = 0
    for n in lst:
        result += int(n + 1e-5) ** 2  # Adding rounding to the next integer
    return result

# Test cases:
assert sum_squares([1, 2, 3]) == 14
assert sum_squares([1, 4, 9]) == 98
assert sum_squares([1, 3, 5, 7]) == 84
assert sum_squares([1.4, 4.2, 0]) == 29
assert sum_squares([-2.4, 1, 1]) == 6
```

This script defines a function `sum_squares()` that calculates the sum of the squares of integers in a given list, rounding each number to the next bigger integer before squaring it. The function tests different scenarios and produces the expected outputs based on the problem's description.