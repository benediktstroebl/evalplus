```python
def monotonic(lst: list) -> bool:
    """Return True is list elements are monotonically increasing or decreasing.
    
    Args:
    lst (list): A list of integers.

    Returns:
    bool: True if the list elements are monotonically increasing or decreasing, False otherwise.
    """
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1)) or \
           all(lst[i] >= lst[i+1] for i in range(len(lst)-1))

# Test cases
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
```

This script defines a function `monotonic` that takes a list of integers as input. It checks if the list elements are monotonically increasing or decreasing by using the `all` function with a generator expression. The `all` function returns `True` if all elements of the iterable are true. The generator expression `lst[i] <= lst[i+1] for i in range(len(lst)-1)` generates pairs of adjacent elements in the list and checks if they are in increasing order. The `or` operator is used to check if the list elements are either monotonically increasing or decreasing.