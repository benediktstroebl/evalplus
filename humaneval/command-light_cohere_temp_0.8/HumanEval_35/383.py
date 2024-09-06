```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test case 1
assert max_element([1, 2, 3]) == 3

# Test case 2
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123
```
This script defines a function `max_element` that takes a list as an argument and returns the maximum element in that list using the `max()` built-in function. The script then provides two test cases to ensure that the function is working correctly.