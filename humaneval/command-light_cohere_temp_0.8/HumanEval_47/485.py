```python
def median(l: list):
    """Return median of elements in the list l.
    assert len(l) > 1,
    mid = len(l) // 2
    if l[mid] > l[-mid]:
        mid = (mid - 1)
    median = (l[mid] + l[mid - 1]) / 2
    return median
```