```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test the function
def test_max_element():
    assert max_element([1, 2, 3]) == 3
    assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123
```
This script defines a function max_element that takes a list l as input and returns the maximum element from the list. It is also includes a test case at the bottom of the script to ensure the correctness of the function. The test_max_element function provides assertions to check the function's output for different input lists.