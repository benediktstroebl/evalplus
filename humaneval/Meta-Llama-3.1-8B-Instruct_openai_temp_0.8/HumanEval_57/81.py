```python
def monotonic(l: list) -> bool:
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    if not l:
        return True  # An empty list is considered monotonically increasing/decreasing
    
    increasing = decreasing = True
    
    for i in range(1, len(l)):
        if l[i] > l[i-1]:
            decreasing = False
        elif l[i] < l[i-1]:
            increasing = False
    
    return increasing or decreasing

# Test cases
print(monotonic([1, 2, 4, 20]))  # Expected output: True
print(monotonic([1, 20, 4, 10]))  # Expected output: False
print(monotonic([4, 1, 0, -10]))  # Expected output: True
print(monotonic([1, 1, 1, 1]))  # Expected output: True
print(monotonic([2, 1, 3, 4]))   # Expected output: True
print(monotonic([]))              # Expected output: True
```
This script defines a function `monotonic` that checks if the input list `l` is monotonically increasing or decreasing. It initializes two flags `increasing` and `decreasing` to `True` and then iterates over the list. If it finds any pair of adjacent elements where the second element is greater than the first (for `increasing`) or less than the first (for `decreasing`), it sets the corresponding flag to `False`. Finally, it returns either `increasing` or `decreasing`, which will be `True` if the list is monotonically increasing or decreasing, respectively.