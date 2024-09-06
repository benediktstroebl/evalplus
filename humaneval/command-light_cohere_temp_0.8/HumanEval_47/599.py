```python
def median(l: list):
    """Return median of elements in the list l"""
    if len(l) < 1:
        raise ValueError("Input list cannot be empty")
    l.sort(l)
    sort(l)
    m = len(l) // 2
    if len(l) % 2 == 0:
        return (l[m] + l[m-1]) / 2
    else:
        return l[m]
```