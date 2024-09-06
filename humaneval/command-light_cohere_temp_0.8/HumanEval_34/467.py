```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    return list(set(sorted(l)))

# Test the function
test_unique = unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
assert test_unique == [0, 2, 3, 5, 9, 123]
```