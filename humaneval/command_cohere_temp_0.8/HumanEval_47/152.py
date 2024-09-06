```python
def median(l: list):
    """Return median of elements in the list l."""
    n = len(l)
    sorted_l = sorted(l)
    if n % 2 == 1:
        return sorted_l[n // 2]
    else:
        mid1 = sorted_l[(n // 2) - 1]
        mid2 = sorted_l[n // 2]
        return (mid1 + mid2) / 2
```