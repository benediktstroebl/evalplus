```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test the function
def test_max_element():
    assert max_element([1, 2, 3]) == 3

# Another test
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123
```
This script defines a function `max_element` that calculates the maximum element in a given list and passes the test with the function `test_max_element` that checks the result of `max_element` function with a list of numbers. 

The `test_max_element` function serves as a unit test for the `max_element` function.