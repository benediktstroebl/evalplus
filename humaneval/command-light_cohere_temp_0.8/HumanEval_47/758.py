```python
def median(l: list):
    """Return median of elements in the list l.
    m = 0
    sum(x for x in l if x >= m) / len(l) if len(l) > 2
    else x
    m = sum(x for x in l) / 2 if len(l) > 1
    return m
```