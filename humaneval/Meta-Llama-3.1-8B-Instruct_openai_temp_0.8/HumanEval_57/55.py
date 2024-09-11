```python
def monotonic(lst: list) -> bool:
    """
    Return True if list elements are monotonically increasing or decreasing.

    Args:
        lst (list): The input list to check for monotonicity.

    Returns:
        bool: True if the list is monotonically increasing or decreasing, False otherwise.

    Examples:
        >>> monotonic([1, 2, 4, 20])
        True
        >>> monotonic([1, 20, 4, 10])
        False
        >>> monotonic([4, 1, 0, -10])
        True
    """
    # Check if list is empty
    if not lst:
        return True  # an empty list is monotonically increasing and decreasing

    increasing = decreasing = True

    # Check if list elements are monotonically increasing
    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            increasing = False

    # Check if list elements are monotonically decreasing
    for i in range(1, len(lst)):
        if lst[i] > lst[i - 1]:
            decreasing = False

    # Return True if list is monotonically increasing or decreasing
    return increasing or decreasing


# Test the function
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
print(monotonic([]))  # True
```

This script defines a function called `monotonic` that checks if a list of numbers is monotonically increasing or decreasing. It does this by iterating over the list and checking if each number is greater than (for increasing) or less than (for decreasing) the previous number. If it finds a pair of numbers where this condition is not met, it sets the corresponding flag (`increasing` or `decreasing`) to `False`. If it finishes checking the list without finding any such pairs, it returns `True`. Otherwise, it returns `False`.