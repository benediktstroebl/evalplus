```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test the function with several lists
assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123]
assert not get_positive([5, 3, -5, 2, -3, 3, -1, 9, 0, 123])

# Test with an empty list
assert get_positive([]) == []
```