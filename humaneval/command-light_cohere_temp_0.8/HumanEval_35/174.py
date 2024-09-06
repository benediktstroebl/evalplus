```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test function for max_element
def test_max_element():
    lst = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    assert max_element(lst) == 123

# Another test function
def test_another_function():
    lst = [-5, 3, -10, 1212123]
    assert max_element(lst) == 1212123
```
This Python code defines a function `max_element` that aims to find the maximum element in the given list. Additionally, there are two test functions, `test_max_element` and `test_another_function`, that use this `max_element` function to pass their respective tests. This code structure allows the reported that the `max_element` function works correctly and passes all tests.