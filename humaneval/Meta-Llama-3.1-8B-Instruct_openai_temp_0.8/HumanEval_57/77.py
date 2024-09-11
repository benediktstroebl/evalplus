```python
def monotonic(lst: list) -> bool:
    """
    Return True if list elements are monotonically increasing or decreasing.

    Args:
        lst (list): The input list.

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

This script defines a function `monotonic` that takes a list as input and returns `True` if the list elements are monotonically increasing or decreasing, and `False` otherwise. The function uses the `all` function with generator expressions to check if all consecutive elements in the list have the same order (either increasing or decreasing). The script includes three test cases to verify the correctness of the function.