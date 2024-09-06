```python
def max_element(lst):
    """Return maximum element in the list."""
    return max(lst, default=float('-inf'))

# Test the function
def test_max_element():
    lst = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    assert max_element(lst) == 123

# Another test with a default value set to negative infinity
test_max_element_default = [5, 3, -5, 2, -3]
test_max_element_default._append(float('-inf'))
assert max_element(test_max_element_default) == float('-inf')
```