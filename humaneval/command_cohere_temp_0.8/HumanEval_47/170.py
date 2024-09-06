```python
def median(l: list):
    """Return median of elements in the list l."""
    l = sorted(l)
    length = len(l)
    if length % 2 == 1:
        return l[length // 2]
    else:
        mid1 = l[length // 2 - 1]
        mid2 = l[length // 2]
        return (mid1 + mid2) / 2
```