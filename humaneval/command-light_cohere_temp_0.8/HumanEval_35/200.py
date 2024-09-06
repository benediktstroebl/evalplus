```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test case 1
assert max_element([1, 2, 3]) == 3

# Test case 2
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

# Test case 3 ( corner case )
assert max_element([-5, -3]) == -5
```
The function takes a list as input and returns the maximum element in the list using the built-in function **max()**. The test cases are also provided to check if the function is working correctly.