```python
def median(l: list):
    """Return median of elements in the list l.
    assert len(l) > 1, "Input list must have more than one element."
    if len(l) % 2 == 1:
        return l[len(l) // 2]
    else:
        return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2
```