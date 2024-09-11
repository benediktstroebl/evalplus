```python
def monotonic(l: list):
    """
    Return True if list elements are monotonically increasing or decreasing.
    
    Args:
        l (list): A list of numbers.
    
    Returns:
        bool: True if list elements are monotonically increasing or decreasing, False otherwise.
    """
    increasing = decreasing = True

    for i in range(1, len(l)):
        # If at any point the list is not increasing or decreasing, return False
        if (l[i] > l[i-1] and not decreasing) or (l[i] < l[i-1] and not increasing):
            return False
        # Update the increasing and decreasing flags
        increasing = l[i] >= l[i-1]
        decreasing = l[i] <= l[i-1]

    return True

# Test cases
print(monotonic([1, 2, 4, 20]))  # Expected output: True
print(monotonic([1, 20, 4, 10]))  # Expected output: False
print(monotonic([4, 1, 0, -10]))  # Expected output: True
```

This script defines a function `monotonic` that checks if the elements in a given list are monotonically increasing or decreasing. It maintains two flags: `increasing` and `decreasing`, which are initially set to `True`. The function iterates over the list, updating these flags as it goes. If it encounters an element that contradicts the current slope of the list (i.e., `l[i] > l[i-1]` when `decreasing` is `True`, or `l[i] < l[i-1]` when `increasing` is `True`), it immediately returns `False`. If the function completes the iteration without finding any contradictions, it returns `True`.