```python
def unique(lst):
    """Return sorted unique elements in a list"""
    return list(set(lst))

# Test cases
def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

test_unique()
```

This script defines a function `unique` that returns a list of unique elements from a given list. The test case `test_unique` includes a few test elements and passes the test with the function.