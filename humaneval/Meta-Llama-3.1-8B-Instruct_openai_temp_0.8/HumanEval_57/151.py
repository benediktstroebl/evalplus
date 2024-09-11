```python
def monotonic(lst: list):
    """
    Return True if list elements are monotonically increasing or decreasing.

    Args:
        lst (list): A list of elements.

    Returns:
        bool: True if list elements are monotonically increasing or decreasing, False otherwise.
    """
    # Check if list is empty or has one element
    if len(lst) < 2:
        return True

    # Check if list is monotonically increasing
    increasing = all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))

    # Check if list is monotonically decreasing
    decreasing = all(lst[i] >= lst[i + 1] for i in range(len(lst) - 1))

    # Return True if list is either monotonically increasing or decreasing
    return increasing or decreasing


# Test cases
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
print(monotonic([1, 1, 1]))  # True
print(monotonic([]))  # True
print(monotonic([1]))  # True
```

This script defines a function `monotonic` that takes a list as input and returns `True` if the list elements are monotonically increasing or decreasing, and `False` otherwise. The function uses list comprehensions to check if the list is monotonically increasing or decreasing, and returns `True` if either condition is met. The script also includes test cases to demonstrate the function's behavior.