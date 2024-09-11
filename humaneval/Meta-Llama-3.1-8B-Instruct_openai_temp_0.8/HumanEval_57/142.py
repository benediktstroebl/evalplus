```markdown
### Monotonic List Checker
#### Checks if a list is monotonically increasing or decreasing

```python
def monotonic(l: list) -> bool:
    """
    Return True if list elements are monotonically increasing or decreasing.
    
    Args:
    l (list): A list of elements.
    
    Returns:
    bool: True if list is monotonically increasing or decreasing, False otherwise.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    
    # Check if list is monotonically increasing
    increasing = all(x <= y for x, y in zip(l, l[1:]))
    
    # Check if list is monotonically decreasing
    decreasing = all(x >= y for x, y in zip(l, l[1:]))
    
    # Check if list is either monotonically increasing or decreasing
    return increasing or decreasing


# Example usage
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
```

This script defines a function `monotonic` that checks if a given list is monotonically increasing or decreasing. It uses the `zip` function to compare each element with its successor in the list and checks if all comparisons are true. The function returns `True` if the list is either monotonically increasing or decreasing and `False` otherwise.