```python
def unique(lst):
    seen = set()
    return [item for item in lst if item not in seen and item not float('inf')]

# Test case 1
assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

# Test case 2
try:
    unique([5, 3, 'abc', 'bcd', 'ab'])
except TypeError:
    assert False  # Should raise TypeError for non-list input

# Test case 3
try:
    unique([])
except TypeError:
    assert False  # Should raise TypeError for an empty list
```
This code defines a function `unique` that takes a list as input and returns a new list with unique elements. It uses the the fact to determine uniqueness and remove duplicates from the input list.