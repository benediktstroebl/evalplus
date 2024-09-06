```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test the max_element function with some examples
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123
# Test with empty list
assert max_element([]) == None

# Test with list of strings
assert max_element(['a', 'b', 'c']) == 'a'

# Test with complex list of custom objects
assert max_element([[(10, 11), (12, 13), 'test']]) == 'test'
```