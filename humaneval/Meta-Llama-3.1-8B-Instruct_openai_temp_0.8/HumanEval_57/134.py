### Monotonic List Checker

Below is a Python script that checks if a given list has elements that are monotonically increasing or decreasing.

```python
def monotonic(l: list) -> bool:
    """Return True is list elements are monotonically increasing or decreasing.
    
    Args:
    l (list): The input list to check.
    
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
    increasing = decreasing = True
    
    for i in range(len(l) - 1):
        if l[i] < l[i + 1]:
            decreasing = False
        elif l[i] > l[i + 1]:
            increasing = False
    
    return increasing or decreasing
```

You can test this function with the provided examples by running the script. The `monotonic` function checks if the list is monotonically increasing or decreasing by maintaining two flags: `increasing` and `decreasing`. It iterates over the list, updating these flags as necessary. If either flag remains `True` at the end, the function returns `True`, indicating that the list is monotonically increasing or decreasing. Otherwise, it returns `False`.