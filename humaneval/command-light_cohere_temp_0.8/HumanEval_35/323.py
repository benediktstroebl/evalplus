```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test function to check if max_element works correctly
def test_max_element(test_list):
    expected = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    actual = max_element(test_list)
    assert expected == actual, "Test failed: Expected {} but got {}".format(expected, actual)

# Test list to run tests
test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
test_max_element(test_list)  # This will pass if the function is correct!
 ``` 
This code defines a function `max_element` that returns the maximum element in the input list, and a test function `test_max_element` that runs the `max_element` function with a test list and asserts the result against the expected output.  This result, the maximum element for any list of numbers should be an integer and greater than any other number, so the output of this function is also an integer.