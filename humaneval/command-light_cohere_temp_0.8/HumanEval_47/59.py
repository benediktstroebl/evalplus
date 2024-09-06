```python
def median(l: list):
    """Return median of elements in the list l.
    assert len(l) >= 1, "List must not be empty"
    assert l[-1] > 0, "Last element of the list must be greater than 0"
    if len(l) % 2 == 1:
        return (l[int(len(l) / 2) - 1] + l[int(len(l) / 2)]) / 2
    else:
        return l[int(len(l) / 2)]
```