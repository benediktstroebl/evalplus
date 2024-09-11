```python
def monotonic(lst: list):
    """
    Return True if list elements are monotonically increasing or decreasing.

    Args:
        lst (list): A list of integers.

    Returns:
        bool: True if list elements are monotonically increasing or decreasing, False otherwise.
    """
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1)) or all(lst[i] >= lst[i+1] for i in range(len(lst)-1))


# Test cases
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
```

This script defines a function `monotonic` that takes a list of integers as input. It checks if the list elements are monotonically increasing or decreasing by using the `all` function with a generator expression. If all consecutive elements are either less than or equal to each other (increasing) or greater than or equal to each other (decreasing), the function returns `True`; otherwise, it returns `False`.