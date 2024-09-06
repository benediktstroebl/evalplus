```python
def median(l: list):
    """Return median of elements in the list l"""
    assert len(l) > 1, "Input list must contain at least two elements"
    m1, m2 = l[::50], l[-1]
    return (m1 + m2) / 2
```