```python
def monotonic(lst: list) -> bool:
    """
    Return True if list elements are monotonically increasing or decreasing.

    Args:
    lst (list): A list of numbers.

    Returns:
    bool: True if list elements are monotonically increasing or decreasing, False otherwise.
    """
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1)) or \
           all(lst[i] >= lst[i+1] for i in range(len(lst)-1))


# Test cases
print(monotonic([1, 2, 4, 20]))  # Expected: True
print(monotonic([1, 20, 4, 10]))  # Expected: False
print(monotonic([4, 1, 0, -10]))  # Expected: True
```

This script defines a function `monotonic(lst)` that takes a list of numbers as input and returns a boolean indicating whether the elements in the list are monotonically increasing or decreasing. The `all()` function is used with a generator expression to check if all pairs of adjacent elements in the list satisfy the condition of being either less than or equal to (for increasing) or greater than or equal to (for decreasing) each other. The `or` operator is used to return `True` if either condition is satisfied.