```python
def monotonic(lst: list) -> bool:
    """
    Return True if list elements are monotonically increasing or decreasing.
    
    Args:
        lst (list): The input list of numbers.
    
    Returns:
        bool: True if list elements are monotonically increasing or decreasing, False otherwise.
    """
    return all(lst[i] - lst[i-1] <= 0 for i in range(1, len(lst))) or \
           all(lst[i] - lst[i-1] >= 0 for i in range(1, len(lst)))

# Test cases
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
```

This script defines a function `monotonic` that takes a list of numbers as input and returns `True` if the list elements are monotonically increasing or decreasing, and `False` otherwise. The function uses a generator expression to check if all consecutive elements in the list have the same sign. The `all()` function returns `True` if all elements of the iterator are true, and `False` otherwise. The `or` operator is used to check both conditions (increasing and decreasing), because a list can be either.