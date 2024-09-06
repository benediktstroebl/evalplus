```python
def median(l: list):
    """Return median of elements in the list l.
    m = len(l)//2
    if m == 0:
        return float('inf')
    return (l[m-1] + l[m]) / 2
```