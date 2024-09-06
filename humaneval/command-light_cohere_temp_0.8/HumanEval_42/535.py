```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    l.append(1)
    return l + [1]  # Single element list with increment
    l.append(1)  # List with two elements with increment
    l.append(1)  # List with three elements with increment
    l.append(1)  # List with four elements with increment
    l.append(1)  # List with five elements with increment
    l.append(1)  # List with six elements with increment
    l.append(1) # List with seven elements with increment
    l.append(1)  # List with eight elements with increment
    l.append(1)  # List with nine elements with increment
```

This script defines a function `incr_list` that takes a list `l` as input and returns a new list with elements from the original list incremented by 1. The function uses the list's built-in `append` method to add the increment value to each element.