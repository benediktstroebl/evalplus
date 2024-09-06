```python
def median(l: list):
    """Return median of elements in the list l"""
    assert len(l) > 1, "Input list must have at least two elements"
    if len(l) % 2 == 1:
        return l[len(l) // 2]
    return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2
```