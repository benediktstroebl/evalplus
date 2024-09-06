```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test the function with some data
test_max_element = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
result = max_element(test_max_element)
assert result == 123
```