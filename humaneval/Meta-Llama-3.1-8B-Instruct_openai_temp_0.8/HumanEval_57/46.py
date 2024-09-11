```python
def monotonic(l: list):
    """
    Return True if list elements are monotonically increasing or decreasing.
    
    Args:
    l (list): A list of numbers.
    
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
        if l[i] > l[i + 1]:
            increasing = False
        if l[i] < l[i + 1]:
            decreasing = False
            
    return increasing or decreasing

# Test the function
print(monotonic([1, 2, 4, 20]))  # Expected: True
print(monotonic([1, 20, 4, 10]))  # Expected: False
print(monotonic([4, 1, 0, -10]))  # Expected: True
```

This script defines a function `monotonic` that checks if the elements in a list are monotonically increasing or decreasing. It iterates over the list and checks each pair of adjacent elements. If it finds a pair where the second element is greater than the first, it sets `increasing` to False. If it finds a pair where the second element is less than the first, it sets `decreasing` to False. If it finishes iterating without changing either `increasing` or `decreasing`, it returns True, indicating that the list is monotonically increasing or decreasing. Otherwise, it returns False.