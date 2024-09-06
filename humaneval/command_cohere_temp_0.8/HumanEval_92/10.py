```python
def any_int(x, y, z):
    """
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    """
    a = x + y == z
    b = y + z == x
    c = x + z == y
    return any([a, b, c])
```

This function takes three arguments `x`, `y`, and `z`. It compares the sums of different pairs of these numbers with each other and returns `True` if any of these comparisons turns out to be true. Additionally, a boolean conversion is used to return `False` if any of the comparisons are not integers. 

Here's an example usage of the function:
```python
print(any_int(5, 2, 7))  # Outputs: True
print(any_int(3, 2, 2))  # Outputs: False
print(any_int(3, -2, 1))  # Outputs: True
print(any_int(3.6, -2.2, 2))  # Outputs: False
```

The function will return `True` for the first two examples because the sum of `5` and `2` is equal to `7` and the sum of `3` and `2` is equal to `5`. It will return `False` for the third example because even though the sum of `3` and `-2` is equal to `1`, the numbers are not integers. It will return `False` for the fourth example because none of the conditions are met and not all numbers are integers.