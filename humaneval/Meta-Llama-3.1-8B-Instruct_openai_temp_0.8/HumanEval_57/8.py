```python
def monotonic(lst: list) -> bool:
    """Return True if list elements are monotonically increasing or decreasing.
    
    Args:
    lst (list): A list of numbers.

    Returns:
    bool: True if list elements are monotonically increasing or decreasing, False otherwise.
    """
    increasing = decreasing = True

    for i in range(len(lst) - 1):
        if lst[i] < lst[i + 1]:
            decreasing = False
        if lst[i] > lst[i + 1]:
            increasing = False

    return increasing or decreasing

# Test cases
print(monotonic([1, 2, 4, 20]))  # Expected: True
print(monotonic([1, 20, 4, 10]))  # Expected: False
print(monotonic([4, 1, 0, -10]))  # Expected: True
```
This script defines a function `monotonic` which checks if the elements in a list are monotonically increasing or decreasing. It uses two flags, `increasing` and `decreasing`, to track whether the list is increasing or decreasing respectively. The flags are initially set to `True` and then updated as the function iterates over the list. If it finds an element that breaks the monotonicity, it sets the corresponding flag to `False`. Finally, the function returns `True` if either of the flags is still `True`, indicating that the list is monotonically increasing or decreasing.