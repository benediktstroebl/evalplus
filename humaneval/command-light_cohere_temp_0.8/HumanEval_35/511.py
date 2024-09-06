```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test the function
test_max_element = max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
assert test_max_element == 123, "Test failed: expected 123, got " + str(test_max_element)
```