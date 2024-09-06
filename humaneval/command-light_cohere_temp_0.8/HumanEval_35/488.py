```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test cases
test_max_element = []
test_max_element.add([1, 2, 3, 5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
test_max_element.add("foo")
def test_function(test_case: list):
    assert max_element(test_case) == test_case[0]
test_max_element.add(test_max_element)

# Run the tests
test_max_element()
``` 
This script defines a function max_element that calculates and returns the maximum element in a given list. The test_max_element test suite verifies that the max_element function operates correctly for various input lists.