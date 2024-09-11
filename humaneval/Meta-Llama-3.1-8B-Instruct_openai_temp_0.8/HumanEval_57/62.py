```python
def monotonic(l: list) -> bool:
    """
    Return True if list elements are monotonically increasing or decreasing.

    Args:
    l (list): A list of numbers.

    Returns:
    bool: True if list elements are monotonically increasing or decreasing, False otherwise.
    """
    # Check if the list is empty
    if len(l) == 0:
        return True

    # Check if the list is monotonically increasing
    increasing = all(l[i] <= l[i + 1] for i in range(len(l) - 1))

    # Check if the list is monotonically decreasing
    decreasing = all(l[i] >= l[i + 1] for i in range(len(l) - 1))

    # Return True if the list is either monotonically increasing or decreasing
    return increasing or decreasing


# Test cases
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
print(monotonic([5, 5, 5, 5]))  # True
print(monotonic([]))  # True
```

This script defines a function `monotonic` that checks if a list of numbers is monotonically increasing or decreasing. It uses list comprehension and the `all` function to check if all elements in the list are either less than or equal to the next element, or greater than or equal to the next element. The function returns `True` if the list meets either of these conditions, and `False` otherwise. The script includes several test cases to demonstrate the function's behavior.