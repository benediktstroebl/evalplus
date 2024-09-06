```python
def median(l: list):
    """Return median of elements in the list l"""
    m = len(l) // 2 + 1
    if m == 1:
        return l[0]
    if m == 2:
        return (l[m - 1] + l[m]) / 2.0
   
    particular tests (see examples in test section)
    return int((l[m // 2 - 1] + l[m // 2]) / 2.0)
```