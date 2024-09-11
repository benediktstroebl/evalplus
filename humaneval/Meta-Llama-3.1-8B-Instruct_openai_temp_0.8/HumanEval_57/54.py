```python
def monotonic(lst: list) -> bool:
    """
    Return True if list elements are monotonically increasing or decreasing.
    
    Args:
    lst (list): A list of numbers.
    
    Returns:
    bool: True if the list elements are monotonically increasing or decreasing, False otherwise.
    """
    increasing = decreasing = True
    
    for i in range(len(lst) - 1):
        if lst[i] < lst[i + 1]:
            decreasing = False
        if lst[i] > lst[i + 1]:
            increasing = False
            
    return increasing or decreasing

# Testing the function
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
```

This Python script defines a function `monotonic` that checks if the elements in a list are either monotonically increasing or decreasing. The function uses two boolean variables `increasing` and `decreasing` to track whether the list elements are monotonically increasing or decreasing, respectively. It then returns `True` if at least one of these conditions is met, and `False` otherwise.