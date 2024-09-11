### Monotonic List Check
#### Python Script
```python
def monotonic(l: list) -> bool:
    """
    Return True if list elements are monotonically increasing or decreasing.
    
    Args:
    l (list): A list of numbers.
    
    Returns:
    bool: True if list elements are monotonically increasing or decreasing, False otherwise.
    """
    increasing = decreasing = True
    
    for i in range(1, len(l)):
        # Check if elements are increasing
        if l[i] < l[i-1]:
            increasing = False
        # Check if elements are decreasing
        elif l[i] > l[i-1]:
            decreasing = False
    
    # Return True if list is either increasing or decreasing
    return increasing or decreasing

# Example usage:
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
```

This script defines a function `monotonic` that checks if a list of numbers is either monotonically increasing or decreasing. It initializes two flags `increasing` and `decreasing` to `True`, assuming the list is both increasing and decreasing at the start. It then iterates over the list from the second element to the end, checking if each element is greater than or less than the previous one. If it finds an element that is out of order, it sets the corresponding flag to `False`. Finally, it returns `True` if either flag is still `True`, indicating that the list is either increasing or decreasing.