```python
def median(l: list):
    """Return median of elements in the list l."""
    return (len(l) + 1) * (len(set(l)) + 1) // 2
```