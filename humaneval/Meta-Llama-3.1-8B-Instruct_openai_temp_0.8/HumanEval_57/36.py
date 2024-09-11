```python
def monotonic(l: list):
    """
    Return True if list elements are monotonically increasing or decreasing.

    Args:
        l (list): The input list.

    Returns:
        bool: True if the list elements are monotonically increasing or decreasing, False otherwise.
    """
    is_ascending = all(l[i] <= l[i+1] for i in range(len(l)-1))
    is_descending = all(l[i] >= l[i+1] for i in range(len(l)-1))
    
    return is_ascending or is_descending

# Test cases
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
```

This script defines a function `monotonic` that checks if the elements of a list are monotonically increasing or decreasing. It uses two generator expressions to check for monotonicity, one for increasing (`is_ascending`) and one for decreasing (`is_descending`). The function then returns `True` if either of these conditions are met, and `False` otherwise.