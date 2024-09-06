```python
def median(l: list):
    """Return median of elements in the list l.
    assert(is != []),
    assert(len(l) >= 1), "List must have at least one element"
    assert(all(isinstance(x, (int, float)) for x in l)), "All elements must be numbers"
    return (l[len(l) // 2] + l[len(l) // 2 - 1]) / 2
```