```python
def unique(lst):
    """Return sorted unique elements in a list"""
    set1 = set(lst)
    return list(set1)

def test_unique():
    lst = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    expected = [0, 2, 3, 5, 9, 123]
    got = unique(lst)
    assert got == expected
```