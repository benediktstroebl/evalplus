```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test case 1:
def test_max_element():
    assert max_element([1, 2, 3]) == 3

# Test case 2:
def test_max_element2():
    assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123
```

This script defines a function `max_element` that takes a list as an argument and returns the maximum element in the list using the `max` function from the built-in `numpy` module. The test cases, `test_max_element` and `test_max_element2`, pass the corresponding tests and demonstrate that the `max_element` function works correctly.