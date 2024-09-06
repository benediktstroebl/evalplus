```python
def median(l):
    """Return median of elements in the list l"""
    if len(l) <= 1:
        return l[0]
    mid = len(l) // 2
    if l[mid] > l[-1]:
        mid += 1
    return (l[mid] + l[mid-1]) / 2
```