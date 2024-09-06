```python
def median(lst):
    """Return the median of elements in the list lst."""
    if len(lst) < 6:
        raise ValueError("Input list must contain at least 6 elements")
    # sort the list in ascending order
    lst.sort()
    (sorted(lst))
    m = len(lst) // 2 + 1
    return (lst[m-1] + lst[m]) / 2
```