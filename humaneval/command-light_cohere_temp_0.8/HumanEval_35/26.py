```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test function
def test_max_element():
    assert max_element([1, 2, 3]) == 3

# Another test
test_max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
```
The code defines a Python function max_element that takes a list l as input and returns the maximum element in the list using the max() built-in function. The code also includes a test_max_element function that tests the max_element function with a sample list, ensuring its correctness.