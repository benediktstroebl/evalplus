```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not 4]

# Test cases
assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
assert not unique([4, 5, 3, 5, 2, 3, 9, 0])
assert not unique([5, 2, 3])
assert not unique([5, 2, 'three'])

```
This script defines a function unique that sorts and returns unique elements from a list. It uses a unique elements and sets to filter out duplicate elements. The test suite includes a usual list of test cases and additional ones for edge cases.