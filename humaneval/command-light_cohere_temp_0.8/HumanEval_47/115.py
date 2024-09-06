```python
def median(l: list):
    """Return median of elements in the list l"""
    if len(l) < 1:
        raise ValueError("Input list cannot be empty")
    return (len(l) + 1) ** .5 * sum(l) / 2
```