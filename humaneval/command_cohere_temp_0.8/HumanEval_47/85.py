```python
def median(l: list):
    """Return median of elements in the list l."""
    sorted_l = sorted(l)
    length = len(sorted_l)
    if length % 2 == 0:
        return (sorted_l[length // 2 - 1] + sorted_l[length // 2]) / 2
    else:
        return sorted_l[length // 2]
```