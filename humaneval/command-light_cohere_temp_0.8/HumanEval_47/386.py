```python
def median(l: list):
    """Return median of elements in the list l.
    m = []
    for x in l:
        m.append(x)
    if len(m) % 2 == 0:
            return float(m[len(m) // 2])
    else:
        return (m[len(m) // 2] + m[len(m) // 2 - 1]) / 2
```