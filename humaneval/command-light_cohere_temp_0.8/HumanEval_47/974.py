```python
def median(l: list):
    """Return median of elements in the list l.
    assert len(l) >= 1, "Input list is empty"
    assert all(isinstance(i, (int, float)) for i in l), "All elements in the list should be numbers"
    if len(l) % 2 == 0:
        return (l[len(l)//2 - 1] + l[len(l)//2]) / 2
    else:
        return l[len(l)//2]
```