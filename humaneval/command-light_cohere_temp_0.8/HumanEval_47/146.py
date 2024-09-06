```python
def median(l: list):
    """Return median of elements in the list l."""
    m = []
    n = len(l)
    for i in range(n):
        if i == n // 2:
            m.append(l[i])
        else:
            m.append(l[i] + (l[n-i-1]) / 2)
    return float(m[n % 2])
```