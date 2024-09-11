```python
def monotonic(lst: list) -> bool:
    """
    Return True if list elements are monotonically increasing or decreasing.
    
    Args:
    lst (list): A list of integers.
    
    Returns:
    bool: True if list elements are monotonically increasing or decreasing, False otherwise.
    """
    increasing = decreasing = True
    
    for i in range(len(lst) - 1):
        if lst[i] < lst[i + 1]:
            decreasing = False
        elif lst[i] > lst[i + 1]:
            increasing = False
    
    return increasing or decreasing

# Example use cases
print(monotonic([1, 2, 4, 20]))  # Expected output: True
print(monotonic([1, 20, 4, 10]))  # Expected output: False
print(monotonic([4, 1, 0, -10]))  # Expected output: True
```

This script defines a function `monotonic` that checks if a list of integers is monotonically increasing or decreasing. It initializes two boolean variables, `increasing` and `decreasing`, to `True`. It then iterates over the list, checking if each element is greater or less than the next one. If it finds an element that is not greater than or not less than the next one, it sets the corresponding boolean variable to `False`. Finally, it returns `True` if either `increasing` or `decreasing` is still `True`, indicating that the list is monotonically increasing or decreasing.