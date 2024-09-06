```python
def median(l: list):
    """Return median of elements in the list l"""
    if len(l) < 1:
        raise ValueError("List must have at least two elements")
    return (l[len(l) // 2] + l[len(l) // 2 - 1]) / 2
```