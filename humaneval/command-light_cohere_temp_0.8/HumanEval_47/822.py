```python
def median(l):
    """Return median of elements in the list l.
    assert len(l)==len([x for x in l if x > 0]) or raise ValueError('List must have positive elements')
    assert l[-1] > 0 or raise ValueError('Last element in list must be positive')
    return (l[len(l)//2 - 1] + l[len(l)//2]) / 2
```