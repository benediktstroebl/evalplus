```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test the max_element function
assert max_element([1, 2, 3]) == 3
assert max_element([5, 3, -5]) == 3
assert max_element([-5, -3, 3, -10]) == 3
assert max_element([123]) == 123
assert max_element([0, 2, 3, 5]) == 3
assert max_element([-10, -3, -5, 0]) == -10
```