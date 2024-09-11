```python
def monotonic(lst: list) -> bool:
    """
    Return True if list elements are monotonically increasing or decreasing.

    Args:
        lst (list): The input list.

    Returns:
        bool: True if the list is monotonically increasing or decreasing, False otherwise.
    """
    is_increasing = all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
    is_decreasing = all(lst[i] >= lst[i+1] for i in range(len(lst)-1))
    return is_increasing or is_decreasing


# Test cases
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
```

This script uses two generator expressions to check if the list is monotonically increasing or decreasing. The `all()` function returns `True` if all elements in the given iterable are true. If any element is false, it immediately returns `False`. 

The `is_increasing` variable checks if all elements in the list are greater than or equal to the next element. Similarly, the `is_decreasing` variable checks if all elements in the list are less than or equal to the next element. Finally, the function returns `True` if either `is_increasing` or `is_decreasing` is `True`, indicating that the list is monotonically increasing or decreasing.