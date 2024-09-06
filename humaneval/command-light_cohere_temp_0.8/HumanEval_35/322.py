```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test the function with various lists
test_max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
assert max_element(test_max_element) == 123

# Test the function with an empty list
test_max_element([])
assert max_element([]) == float('-inf'))

# Test the function with a list of strings
test_max_element(["hi", "hello", "world!oaar!worldo!th")
assert max_element(test_max_element) == "hello"
```