```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test the function with a list of mixed numbers
test_max_element = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
assert max_element(test_max_element) == 123

# Test the function with a list of numbers
test_single_element = [5, -5, -10]
assert max_element(test_single_element) == -5
```