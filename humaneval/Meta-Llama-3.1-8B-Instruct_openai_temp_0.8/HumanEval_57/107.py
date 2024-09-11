```python
def monotonic(l: list):
    """Return True if list elements are monotonically increasing or decreasing.
    
    Args:
    l (list): A list of elements
    
    Returns:
    bool: True if list elements are monotonically increasing or decreasing, False otherwise
    
    Examples:
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    if not l:  # check if list is empty
        return True
    
    increasing = decreasing = True
    
    for i in range(1, len(l)):
        if l[i] < l[i - 1]:
            increasing = False
        if l[i] > l[i - 1]:
            decreasing = False
    
    return increasing or decreasing


# Test cases
print(monotonic([1, 2, 4, 20]))  # Expected output: True
print(monotonic([1, 20, 4, 10]))  # Expected output: False
print(monotonic([4, 1, 0, -10]))  # Expected output: True
print(monotonic([]))  # Expected output: True
print(monotonic([10]))  # Expected output: True
print(monotonic([10, 10, 10]))  # Expected output: True
```

This script checks if the elements in the list are monotonically increasing or decreasing. It does this by comparing each element with its previous one. If the list is empty or contains only one element, it returns True because there are no elements to compare. Otherwise, it checks if all elements are in increasing or decreasing order by setting two flags (`increasing` and `decreasing`) to True initially. If it encounters a pair of elements that are not in increasing or decreasing order, it sets the corresponding flag to False. Finally, it returns True if either `increasing` or `decreasing` is still True, and False otherwise.