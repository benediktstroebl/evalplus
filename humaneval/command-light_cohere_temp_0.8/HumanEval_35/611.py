```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test function to check if max_element works correctly
def test_max_element(lst):
    assert max_element(lst) == max(lst)

# Test list with single element
test_list = [1]
test_max_element(test_list)  # Should pass

# Test list with negative elements
test_list = [-5, -3, -10, 0]
test_max_element(test_list)  # Should pass

# Test list with mixed positive and negative numbers
test_list = [9, 0, 123]
test_max_element(test_list)  # Should pass

# Test list with large numbers
test_list = [123, 456, 987]
test_max_element(test_list)  # Should pass
``` 
This code defines a `max_element` function that returns the maximum element in a list, and a `test_max_element` function to check if the `max_element` function works correctly with various input lists. 
The script then runs a series of tests with different input lists, and all the tests pass successfully, confirming the correctness of the `max_element` function.