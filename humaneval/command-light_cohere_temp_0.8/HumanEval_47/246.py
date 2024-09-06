```python
def median(l):
    """Return median of elements in the list l"""
    m = []
    for x in l:
        m.append(x[m: (m + x) // 2])
    return float(m[-1])
```