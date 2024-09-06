```python
def median(l: list):
    """Return median of elements in the list l.
    assert len(l) > 1,  
    assert len(set(l)) == len(l), "List must be unique"
    return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2
```