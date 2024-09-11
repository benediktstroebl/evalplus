```python
def monotonic(l: list):
    """
    Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    if len(l) < 2:
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
print(monotonic([1]))  # Expected output: True
print(monotonic([1, 1, 1]))  # Expected output: True
```

This script defines a function `monotonic` that checks if a list's elements are monotonically increasing or decreasing. It first checks if the list has less than 2 elements (in which case it's considered monotonic). Then, it iterates over the list to check if there are any pairs of elements that don't follow either the increasing or the decreasing pattern. If such a pair is found, the respective flag is set to `False`. Finally, the function returns `True` if either the increasing or the decreasing flag is still `True`, indicating that the list's elements are monotonically increasing or decreasing.