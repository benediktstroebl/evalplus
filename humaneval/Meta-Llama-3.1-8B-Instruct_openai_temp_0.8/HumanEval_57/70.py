### Monotonic List Checker
#### Python Script

```python
def monotonic(l: list):
    """Return True if list elements are monotonically increasing or decreasing.
    
    Args:
        l (list): List of numbers to check.
    
    Returns:
        bool: True if list elements are monotonically increasing or decreasing, False otherwise.
    """
    increasing = decreasing = True
    
    for i in range(1, len(l)):
        if l[i] < l[i - 1]:
            increasing = False
        if l[i] > l[i - 1]:
            decreasing = False
    
    return increasing or decreasing

# Example usage:
if monotonic([1, 2, 4, 20]):
    print("List elements are monotonically increasing or decreasing.")
else:
    print("List elements are not monotonically increasing or decreasing.")

if monotonic([1, 20, 4, 10]):
    print("List elements are monotonically increasing or decreasing.")
else:
    print("List elements are not monotonically increasing or decreasing.")

if monotonic([4, 1, 0, -10]):
    print("List elements are monotonically increasing or decreasing.")
else:
    print("List elements are not monotonically increasing or decreasing.")
```

This script defines a function `monotonic` that checks if the elements in a list are monotonically increasing or decreasing. It uses two flags, `increasing` and `decreasing`, to track whether the list is increasing or decreasing, respectively. The function iterates over the list, updating these flags as it encounters elements that contradict the current monotonic trend. Finally, it returns `True` if either `increasing` or `decreasing` is `True`, indicating that the list is monotonically increasing or decreasing.