```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not == 0]

# Test cases
assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
assert not unique([5, 3, 5, 2, 'abc', 3, 9, 0])
assert not unique([1, 2, 3, 'abc', 4, 5])
assert not unique([])
```
The function `unique` uses a set to keep track of elements it has seen, then returns a new list with all elements that are not in the set (and not 0) in the original list.