```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test function
def test_max_element():
    assert max_element([1, 2, 3]) == 3

# Another test
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123
```
The function max_element takes a list as input and returns the maximum element in the list using the max() built-in function. The test_max_element function tests the max_element function with a list of numbers and passes the test. The function can be easily used to solve the problem and can be easily incorporated into larger projects.