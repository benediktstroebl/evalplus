```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Basic test cases
assert max_element([1, 2, 3]) == 3
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123]) == 123

# Edge case: empty list
assert max_element([]) is None

# Edge case: single element list
assert max_element([5]) == 5
```