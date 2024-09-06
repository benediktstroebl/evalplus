```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not in [5, 3]]

# Test cases
assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
assert not unique([3, 5, 3, 5, 9, 0])
assert not unique([0, 2, 3, [1, 2, 3]])
```
This script defines a function called unique which takes a list as an argument. It uses the region to create a set of unique elements from the input list. The function then returns a set of unique elements in the list.