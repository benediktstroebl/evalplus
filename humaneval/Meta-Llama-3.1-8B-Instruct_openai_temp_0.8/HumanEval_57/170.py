```python
def monotonic(l: list):
    """
    Return True if list elements are monotonically increasing or decreasing.
    
    Args:
    l (list): A list of elements to check for monotonicity.
    
    Returns:
    bool: True if the list elements are monotonically increasing or decreasing, False otherwise.
    """
    if not l:  # edge case: an empty list is considered monotonically increasing/decreasing
        return True
    
    increasing = decreasing = True
    
    for i in range(1, len(l)):
        if l[i] < l[i - 1]:
            increasing = False
        if l[i] > l[i - 1]:
            decreasing = False
        
        # if the list is neither increasing nor decreasing, return False
        if not increasing and not decreasing:
            return False
    
    return increasing or decreasing

# Test cases
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
```

This Python script defines a function `monotonic` that takes a list `l` as input and returns `True` if the list elements are monotonically increasing or decreasing and `False` otherwise. The function iterates through the list and checks for consecutive elements that are not in order. If such elements are found, it sets the `increasing` and `decreasing` flags to `False`. If both flags are still `True` after checking all elements, it means the list is monotonically increasing or decreasing, so the function returns `True`. Otherwise, it returns `False`. The test cases demonstrate the function's behavior on different inputs.