```python
def median(l: list):
    """Return median of elements in the list l."""
    sorted_l = sorted(l)
    length = len(sorted_l)
    if length % 2 == 1:
        return sorted_l[length // 2]
    else:
        mid1 = sorted_l[(length // 2) - 1]
        mid2 = sorted_l[length // 2]
        return (mid1 + mid2) / 2
```