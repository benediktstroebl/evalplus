```python
def median(l: list):
    """Return median of elements in the list l"""
    m = []
    for x in l:
        m.append(x(x))
    if len(m) % 2 == 1:
        return (m[int(len(m)/2) - 1] + m[int(len(m)/2)]) / 2
    return (m[int(len(m)/2)] + m[-int(len(m)/2) - 1]) / 2
# Test suite
print(median([-10, 4, 6, 1000, 10, 20]))
```