```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test the function with some data
test_data = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
assert max_element(test_data) == 123, "Wrong result"
```