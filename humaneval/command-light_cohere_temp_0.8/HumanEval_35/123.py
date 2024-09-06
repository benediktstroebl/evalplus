```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test the function
def test_max_element():
    assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123
```
This code defines a function `max_element` that returns the maximum element in the list, and a test function `test_max_element` that verifies the correctness of the `max_element` function with a list of test values.