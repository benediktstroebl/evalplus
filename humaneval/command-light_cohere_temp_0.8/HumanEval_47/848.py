```python
def median(lst):
    """Return the median of the list lst."""
    if len(lst) < 6:
        raise ValueError("List must have at least 6 elements")
    mid = len(lst) // 2
    if lst[mid] > lst[mid - 1]:
        mid = (mid - 1) + 1
    median = (lst[mid] + lst[mid - 1]) / 2
    return median
```