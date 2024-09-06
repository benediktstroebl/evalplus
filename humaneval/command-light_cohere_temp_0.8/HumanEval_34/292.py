```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not in set()]
    # remove duplicates, then sort
    seen.sort()
    unique_dedup([5, 3, 5, 2, 3, 3, 9, 0, 123])
    assert len(unique([5, 3, 5, 2, 3, 3, 9, 0, 123])) ==  6  # all numbers are unique
assert len(unique([5, 3, 5, 2, 3, 3, 9, 0, 1,2,3])) ==  5  # duplicate removed
assert len(unique([3, 3, 3, 4, 7, 9, 2])) ==  2  # should have only one 3
```