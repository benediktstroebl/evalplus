```python
def max_element(lst):
    """Return maximum element in the list."""
    return max(lst)

# Test the function with various inputs
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123
# Test with empty list
assert max_element([]) == 0
# Test with single element list
assert max_element([1]) == 1
```