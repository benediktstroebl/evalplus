```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test function
def test_max_element():
    test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    expected = 123
    got = max_element(test_list)
    assert got == expected, "max element is not equal"

# Run the test function
test_max_element()
``` 
This script defines a function max_element that returns the maximum element in a given list. It also includes a test function that creates a test list and passes the max_element function with this list, and checks if the maximum element is correct.