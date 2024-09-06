```python
def median(l: list):
    """Return median of elements in the list l."""
    m = len(l) // 2 + 1
    return l[(m-1) * 2]
```