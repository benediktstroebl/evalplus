```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test the function
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123
# Test with empty list
assert max_element([]) is None

# Test with a list of strings
assert max_element(["Hello", "World!"]) == "World!"
```