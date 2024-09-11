```python
def monotonic(l: list):
    """Return True if list elements are monotonically increasing or decreasing.
    
    Args:
    l (list): A list of numbers.
    
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
    # Check if the list is empty
    if len(l) < 2:
        return True

    increasing = decreasing = True

    # Iterate over the list to check for monotonicity
    for i in range(len(l) - 1):
        # Check if the list is increasing
        if l[i] < l[i + 1]:
            decreasing = False
        # Check if the list is decreasing
        elif l[i] > l[i + 1]:
            increasing = False
        # If the list is neither increasing nor decreasing, return False
        else:
            return False

    # Return True if the list is either increasing or decreasing
    return increasing or decreasing
```

In this script, we first check if the list is empty. If the list is empty or contains only one element, it is considered monotonically increasing or decreasing, so we return `True`.

Then, we initialize two boolean variables, `increasing` and `decreasing`, both set to `True`. We iterate over the list, checking each pair of adjacent elements. If we find a pair where the first element is less than the second, we set `decreasing` to `False`. If we find a pair where the first element is greater than the second, we set `increasing` to `False`. If we find a pair where the first element is equal to the second, we immediately return `False`, as the list is not monotonically increasing or decreasing.

Finally, we return `True` if the list is either increasing or decreasing.