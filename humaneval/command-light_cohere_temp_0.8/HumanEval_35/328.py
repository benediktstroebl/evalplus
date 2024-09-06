```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test the function with a list of numbers
test_max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
assert max_element(test_max_element) == 123

# Test the function with a list of strings
test_max_element(['A', 'B', 'E'])
assert max_element(test_max_element) == 'E'

# Test the function with a custom data structure
test_max_element([None, 'hello', 'world'])
assert max_element(test_max_element) == 'world'
```