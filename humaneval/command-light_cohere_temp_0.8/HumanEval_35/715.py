```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test cases
assert max_element([1, 2, 3]) == 3
assert max_element([5, 3, -5]) == 3
assert max_element([-5, -3, 3, 5, 3]) == 3
assert max_element([0, 2, 3, 7]) == 3
assert max_element([123, 0, 2, 1]) == 2
assert max_element([-10, -3, -5, -2, 3]) == -5
```