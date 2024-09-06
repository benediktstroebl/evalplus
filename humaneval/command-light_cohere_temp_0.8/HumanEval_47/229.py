```python
def median(l: list):
    """Return median of elements in the list l.
    l = [list](l)
    n = len(l)
    if n % 2 == 0:
        median_ = (l[n//2 - 1] + l[n//2]) / 2
    else:
        median_ = l[n//2]
    return median_
```