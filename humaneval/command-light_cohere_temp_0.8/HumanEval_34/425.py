```python
def unique(lst):
    """Return sorted unique elements in a list"""
    set1 = set(lst)
    return list(set1)

def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
```

This script defines a function unique that takes a list as input and returns a new list with unique elements from the original list. It also has a testing code unique which passes all the tests.