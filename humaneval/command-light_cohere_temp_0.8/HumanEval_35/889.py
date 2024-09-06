```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test the function
def test_max_element():
    assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123
```

This code defines a function `max_element` that returns the maximum element in the input list. The `test_max_element` test function passes the test by verifying that the output of `max_element` is equal to the expected maximum element `123` in the input list.