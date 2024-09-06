```python
def unique(lst):
    """Return sorted unique elements in a list"""
    return list(set(sorted(lst)))

def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
```
This code provides a unique function that sorts and returns unique elements from an input list. The test_unique function tests the also.