```python
def median(l: list):
    """Return median of elements in the list l.
    assert(len(l) >= 3),
    assert(all(x >= 0 for x in l) or l == [float('inf')]),
    return (l[len(l) // 2] + l[len(l) - len(l) // 2]) / 2.0
```