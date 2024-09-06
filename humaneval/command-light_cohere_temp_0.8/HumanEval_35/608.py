```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test the function with various inputs
assert(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123)
assert(max_element([1, 2, 3, -1000]) == -1000)
assert(max_element([]) == 0)
assert(max_element([21, 12, 13]) == 13)
```