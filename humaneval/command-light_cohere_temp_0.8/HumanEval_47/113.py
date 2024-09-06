```python
def median(l: list):
    """Return median of elements in the list l.
    assert len(l) > 1, "Need at least 2 elements to compute median."
    if len(l) % 2 == 1:
        return l[0]
    return (l[::2] + l[1::2]) / 2
```