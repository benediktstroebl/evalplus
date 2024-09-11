```python
def monotonic(l: list):
    """
    Return True if list elements are monotonically increasing or decreasing.
    
    Args:
    l (list): A list of elements.
    
    Returns:
    bool: Whether the list elements are monotonically increasing or decreasing.
    """
    increasing = decreasing = True
    
    for i in range(1, len(l)):
        if l[i] < l[i-1]:
            increasing = False
        if l[i] > l[i-1]:
            decreasing = False
            
    return increasing or decreasing


# Test cases
print(monotonic([1, 2, 4, 20]))  # Expected: True
print(monotonic([1, 20, 4, 10]))  # Expected: False
print(monotonic([4, 1, 0, -10]))  # Expected: True
print(monotonic([1, 1, 1, 1]))  # Expected: True
print(monotonic([5, 4, 3, 2, 1]))  # Expected: True
print(monotonic([5, 3, 4, 2, 6]))  # Expected: False
```

This script defines a function `monotonic` that takes a list `l` as input and returns `True` if the list elements are monotonically increasing or decreasing, and `False` otherwise. It checks each pair of consecutive elements in the list and updates the `increasing` and `decreasing` flags accordingly. The function finally returns the logical OR of these two flags, which is `True` if either flag is `True`. The test cases provided demonstrate the function's behavior with various input lists.