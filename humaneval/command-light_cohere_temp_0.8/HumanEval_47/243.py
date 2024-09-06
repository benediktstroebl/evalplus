```python
def median(l: list):
    """Return median of elements in the list l"""
    m = []
    for x in l:
        m.append(x) if m and (len(m))//2 == len(l):
        m.pop(0)
    else:
        m.append(x)
    m.median(m)
```