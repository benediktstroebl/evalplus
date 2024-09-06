```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test the function with various inputs
test_max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
test_max_element([])
test_max_element([5, 9, 2, -9, 3, -3])
test_max_element([1, 2, 3, -4, -5])
test_max_element([10, 2, 3, -1, 0, -43])
```
The `max_element` function takes a list as input and returns the maximum element in the list using the `max` function. The test cases ensure the theme that the function correctly identifies the maximum element in each list.