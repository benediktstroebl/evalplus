```python
def monotonic(lst: list) -> bool:
    """Return True if list elements are monotonically increasing or decreasing.
    
    Args:
        lst (list): A list of numbers.
    
    Returns:
        bool: True if the list is monotonically increasing or decreasing, False otherwise.
    """
    increasing = decreasing = True
    
    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            increasing = False
        if lst[i] > lst[i - 1]:
            decreasing = False
    
    return increasing or decreasing

# Example use cases
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
```

In this script, the function `monotonic` checks whether the input list is monotonically increasing, decreasing, or neither. It iterates over the list, maintaining two flags: `increasing` and `decreasing`. The function returns `True` if the list is monotonically increasing or decreasing, and `False` otherwise. The example use cases demonstrate the function's usage.