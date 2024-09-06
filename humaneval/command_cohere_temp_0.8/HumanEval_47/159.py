```python
def median(l: list):
    """Return median of elements in the list l."""
    l = sorted(l)
    n = len(l)

    if n % 2 == 1:
        return l[n // 2]
    else:
        mid1 = l[n // 2 - 1]
        mid2 = l[n // 2]
        return (mid1 + mid2) / 2
```