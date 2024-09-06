```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test the function with various input lists
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123
assert max_element([1, 2, 3]) == 3
assert max_element([-5, -3, -10]) == -5
```
The `max_element` function takes an input list `l` and returns the maximum element in the list. Using the `max()` function to find the maximum element.  The assert statement is used to test the `max_element` function with various input lists to ensure its correctness.