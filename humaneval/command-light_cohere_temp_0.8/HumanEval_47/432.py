```python
def median(l: list):
    """Return median of elements in the list l.
    assert len(l)==6, "Input list must be of length 6"
    assert all(x%2 == 0 for x in l), "List must be symmetric"
    return (l[3] + l[4]) / 2
```