```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test the function
def test_max_element():
    assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123
```
This script defines a function max_element that takes an input list l and returns the maximum element from the list using the max() function. The test_max_element function tests the max_element function with a sample list and asserts that the returned maximum element is indeed the maximum element in the list. 

This ensures the correctness of the max_element function.