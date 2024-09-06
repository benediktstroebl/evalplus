```python
def median(l: list):
    """Return median of elements in the list l."""
    l = sorted(l)
    length = len(l)
    if length % 2 == 0:
        return (l[length // 2 - 1] + l[length // 2]) / 2
    else:
        return l[length // 2]
```