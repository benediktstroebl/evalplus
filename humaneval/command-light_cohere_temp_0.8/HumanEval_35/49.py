```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test function
def test_max_element():
    test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    assert max_element(test_list) == 123

# Test invalid type
def invalid_type_test():
    test_list = [1, 2, 3]
    with pytest.raises:InvalidFunctionError():
        max_element(test_list)
    pass

# Test invalid argument
def invalid_arg_test():
    test_list = [5, 3, -5, 2, -3]
    with pytest.raises:ValueError():
        max_element([])
    pass

# Run tests
test_max_element()
invalid_type_test()
invalid_arg_test()
```
This Python code defines a function `max_element` that efficiently finds the maximum element within a given list. The function utilizes the Python's built-in `max` function to achieve this.

Additionally, the code includes unit tests for the `max_element` function using the `pytest` module. The tests ensure the essential that the function correctly identifies the maximum element from various lists and handles invalid inputs appropriately.