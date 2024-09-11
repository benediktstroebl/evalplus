```python
def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    return all(x <= y for x, y in zip(l, l[1:])) or all(x >= y for x, y in zip(l, l[1:]))

# Test cases
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
```

This script uses Python's built-in `zip()` function to pair adjacent elements in the list, and then checks if all these pairs satisfy the condition for monotonicity. The `all()` function returns `True` if all elements of the iterable are true. If the list is empty or contains only one element, the function returns `True` because a list with one element is considered monotonic.