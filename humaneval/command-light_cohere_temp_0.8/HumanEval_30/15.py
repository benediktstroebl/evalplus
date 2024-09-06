```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

# Test the function with various input
test_get_positive = get_positive

test_get_positive([-1, 2, -4, 5, 6])
assert test_get_positive == [2, 5, 6]

test_get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
assert test_get_positive == [5, 3, 2, 3, 9, 123, 1]

# Test with a dict input
test_get_positive({-2: 10, 5: 8, -3: 6})
assert test_get_positive == [-2, 10, 5]

test_get_positive({5: 8, -3: 6, 0: 7})
assert test_get_positive == [0, 8, -3]
```