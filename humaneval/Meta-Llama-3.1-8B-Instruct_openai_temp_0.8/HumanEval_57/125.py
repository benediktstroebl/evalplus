```python
def monotonic(lst: list) -> bool:
    """
    Return True if list elements are monotonically increasing or decreasing.

    Args:
        lst (list): A list of numbers.

    Returns:
        bool: True if the list elements are monotonically increasing or decreasing, False otherwise.
    """
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1)) or \
           all(lst[i] >= lst[i + 1] for i in range(len(lst) - 1))


# Test cases
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
```

This script uses Python's built-in `all` function to check if all pairs of adjacent elements in the list satisfy the monotonic condition. The `all` function returns `True` if all elements of the iterable are true. If at least one element is false, it returns `False`. 

The `or` operator is used to check for both increasing and decreasing lists. If either condition is met, the function returns `True`. If neither condition is met, the function returns `False`.