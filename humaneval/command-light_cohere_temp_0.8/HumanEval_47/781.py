```python
def median(lst):
    """Return the median of list lst."""
    if len(lst) < 3:
        raise ValueError("Input list must have at least 3 elements.")

    mid = len(lst) // 2
    left = lst[mid - 1]
    right = lst[mid]
    if lst[mid - 2] > right:
        left, right = right, left
    return (left + right) / 2
```