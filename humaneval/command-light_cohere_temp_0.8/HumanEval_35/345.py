```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test the function with various lists
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

# Test with empty list
assert max_element([]) is None

# Test with list of strings
assert max_element(['hi', 'hello', 'world! !', '!python']) == 'hello'
```