```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test the function with several lists
test_max_element = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
assert max_element(test_max_element) == 123

# Test with empty list
test_empty = []
assert max_element(test_empty) == float('-inf')

# Test with list of strings
test_strings = [" Hello", "World", "!!! "]
assert max_element(test_strings) == "!"
```