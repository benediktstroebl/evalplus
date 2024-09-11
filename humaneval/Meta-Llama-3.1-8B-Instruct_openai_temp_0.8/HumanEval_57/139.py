```python
def monotonic(lst: list):
    """
    Return True if list elements are monotonically increasing or decreasing.
    
    Args:
    lst (list): A list of numbers.
    
    Returns:
    bool: True if the list is monotonically increasing or decreasing, False otherwise.
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

This script defines a function `monotonic` that takes a list of numbers as input and returns a boolean indicating whether the list is monotonically increasing or decreasing. It uses two flags, `increasing` and `decreasing`, to track whether the list is currently increasing or decreasing. If it encounters a pair of elements where one is smaller than the previous one, it sets `decreasing` to `False`; if it encounters a pair of elements where one is larger than the previous one, it sets `increasing` to `False`. Finally, it returns the logical OR of `increasing` and `decreasing`, which will be `True` if and only if the list is monotonically increasing or decreasing.