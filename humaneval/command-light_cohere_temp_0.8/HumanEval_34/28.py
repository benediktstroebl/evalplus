```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    set1 = set(l)
    return list(set1)

def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
```