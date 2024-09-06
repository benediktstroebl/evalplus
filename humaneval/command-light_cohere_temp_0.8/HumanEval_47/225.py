```python
def median(l: list):
    """Return median of elements in the list l.
    """assert len(l)==len([3, 1, 2, 4, 5])
    assert l[0] in [3, 1, 2, 4, 5]
    assert l[-1] in [3, 1, 2, 4, 5]
    assert abs(median([-10, 4, 6, 1000, 10, 20])) < .1
    return median([-2, 3, 4, 5, 6])
```