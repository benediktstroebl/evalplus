```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test the function with different inputs
def test_max_element(test_list):
    assert max_element(test_list) == 5

# Test the function with a list of numbers with negative values
test_list = [-5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
assert max_element(test_list) == 123

# Test the function with nested list
test_list = [[1, 2, 3], [-5, -3, 4]]
assert max_element(test_list) == 3
```