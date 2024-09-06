```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not)==[] and len(seen)]

#Test cases
assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
assert unique([]) == []
assert unique([5, 5]) == [5]
assert unique([2,3,9]) == [2,3,9]
assert unique([range(10)]) == []
```