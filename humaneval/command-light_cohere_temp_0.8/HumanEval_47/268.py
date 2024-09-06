```python
def median(l: list):
    """Return median of elements in the list l"""
    m = []
    n = len(l)
    for i in range(n // 2):
        m.append(l[i])
    if n&1:
        m.append(l[-1])
    m.sort()
    value = m[len(m)/2
    return float(value)
```