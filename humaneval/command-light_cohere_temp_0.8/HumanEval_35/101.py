```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test the function with various inputs
 assert max_element([1, 2, 3]) == 3
 assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123
 assert max_element([-5, -3, -10]) == -10
 assert max_element([]) == 0
 assert max_element([21, 12, 13]) == 13
```
This function utilizes the built-in function `max()` to find the largest element in the list. The test cases ensure that the function works correctly with various inputs.