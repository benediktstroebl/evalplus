```python
def median(lst):
    """Return the median of elements in the list lst."""
    if len(lst) < 6:
        raise ValueError("Input list must contain at least 6 elements")
    return (lst[(len(lst) + 1) // 2] + lst[(len(lst) + 1) // 2 + 1]) / 2
```