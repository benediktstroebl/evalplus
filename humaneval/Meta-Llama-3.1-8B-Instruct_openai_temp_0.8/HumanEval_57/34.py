```python
def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    
    Args:
    l (list): The list to check for monotonicity.
    
    Returns:
    bool: True if the list elements are monotonically increasing or decreasing, False otherwise.
    
    Examples:
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    increasing = decreasing = True
    
    for i in range(len(l) - 1):
        if l[i] < l[i + 1]:
            decreasing = False
        if l[i] > l[i + 1]:
            increasing = False
    
    return increasing or decreasing

# Test cases
print(monotonic([1, 2, 4, 20]))  # Expected True
print(monotonic([1, 20, 4, 10]))  # Expected False
print(monotonic([4, 1, 0, -10]))  # Expected True
```

In this script, we define a function `monotonic` that checks if the elements in the input list `l` are monotonically increasing or decreasing. We initialize two boolean variables, `increasing` and `decreasing`, to `True`, assuming that the list is monotonically increasing and decreasing initially. Then we iterate through the list, checking if each element is less than or greater than the next element. If we find an element that is greater than the next one, we set `increasing` to `False`, and if we find an element that is less than the next one, we set `decreasing` to `False`. Finally, we return `True` if `increasing` or `decreasing` is still `True`, meaning that the list is monotonically increasing or decreasing. Otherwise, we return `False`.