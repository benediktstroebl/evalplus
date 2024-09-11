```python
def monotonic(lst: list):
    """
    Return True if list elements are monotonically increasing or decreasing.

    Args:
        lst (list): Input list

    Returns:
        bool: True if list elements are monotonically increasing or decreasing, False otherwise

    Example:
        >>> monotonic([1, 2, 4, 20])
        True
        >>> monotonic([1, 20, 4, 10])
        False
        >>> monotonic([4, 1, 0, -10])
        True
    """
    
    increasing = decreasing = True

    for i in range(1, len(lst)):
        # If the current element is smaller than the previous one, the list is not increasing
        if lst[i] < lst[i-1]:
            increasing = False
        # If the current element is greater than the previous one, the list is not decreasing
        if lst[i] > lst[i-1]:
            decreasing = False

    # Return True if the list is either increasing or decreasing
    return increasing or decreasing


# Test cases
if monotonic([1, 2, 4, 20]):
    print("Test case 1: True")
else:
    print("Test case 1: False")

if monotonic([1, 20, 4, 10]):
    print("Test case 2: True")
else:
    print("Test case 2: False")

if monotonic([4, 1, 0, -10]):
    print("Test case 3: True")
else:
    print("Test case 3: False")
```

This script defines a function `monotonic` that checks if a list is monotonically increasing or decreasing. It then tests this function with the three example use cases provided in the problem statement.