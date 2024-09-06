```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test cases
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

# Test lists with only negative elements
assert max_element([-5, -3, -10]) == -10

# Test empty list
assert max_element([]) == None

# Test lists with one element
assert max_element([1]) == 1
```