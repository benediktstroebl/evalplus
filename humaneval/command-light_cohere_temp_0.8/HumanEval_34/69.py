```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not:]

# Test cases
assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
assert not unique([1, 2, 3, 4, 5])
assert not unique([])
assert not equal(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]), [0, 2, 3, 5, 9, 123])
```