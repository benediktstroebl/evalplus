```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not == float('inf')]

# Test 1
assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

# Test 2
assert unique([]) == []

# Test 3
assert unique([1, 2, 3, 4, 5]) == [1, 2, 3]

# Test 4
try:
    unique([5, 3, 'abc'])
except TypeError:
    assert False  # expected error
```