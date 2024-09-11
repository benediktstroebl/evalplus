```python
def monotonic(l: list):
    """
    Return True is list elements are monotonically increasing or decreasing.

    Args:
        l (list): A list of numbers.

    Returns:
        bool: True if list elements are monotonically increasing or decreasing, False otherwise.

    Examples:
        >>> monotonic([1, 2, 4, 20])
        True
        >>> monotonic([1, 20, 4, 10])
        False
        >>> monotonic([4, 1, 0, -10])
        True
    """
    return all(l[i] <= l[i+1] for i in range(len(l)-1)) or all(l[i] >= l[i+1] for i in range(len(l)-1))

# Test cases
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
```

In this script, the function `monotonic` takes a list of numbers as input. It checks two conditions: 

1. All elements in the list are less than or equal to their succeeding elements (monotonically increasing).
2. All elements in the list are greater than or equal to their succeeding elements (monotonically decreasing).

The `all` function is used to check if all elements satisfy a given condition. If either of the conditions is met, the function returns `True`, otherwise, it returns `False`.

The test cases at the end of the script demonstrate the function's behavior with different inputs.