```python
def median(l: list):
    """Return median of elements in the list l."""
    return (sorted(l) + [0])[len(l) // 2]
```