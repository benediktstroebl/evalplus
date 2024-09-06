```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test cases for max_element function
assert max_element([1, 2, 3]) == 3
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123]) == 123
assert max_element([-10, -5, -3, -2, -1]) == -10
```
The function max_element, accepts a list as an argument and uses the built-in function max to return the maximum element in the list. The test cases ensure the time, that the max_element function is correctly implemented.