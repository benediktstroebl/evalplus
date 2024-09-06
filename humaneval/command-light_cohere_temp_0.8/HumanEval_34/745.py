```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not in [-None, -LLONG_MIN, -LLONG_MAX]]

# Tests
assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
assert not unique([]) == []
assert not unique([5, 3, 'abc']) == []
assert not unique([-1, 0]) == []
assert not unique([-5, 5]) == [-5]
```