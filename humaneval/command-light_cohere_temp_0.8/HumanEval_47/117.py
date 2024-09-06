```python
def median(l):
    """Return median of elements in the list l.
    if len(l) < 1:
        raise ValueError("Input list must have at least two elements")
    if len(l) == 1:
        return l[0]
    mid = len(l) // 2
    left = l[:mid]
    right = l[mid:]
    return (left + right) / 2
```