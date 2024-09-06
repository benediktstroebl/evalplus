```python
def median(l):
    """Return median of elements in the list l.
    if len(l) <= 1:
        return l[0]
    return (len(l) + 1) / 2.0 * (l[len(l) // 2] + l[(len(l) - 1) // 2])
```