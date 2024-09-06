```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test the function with a list of various numbers
test_max_element = max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
assert test_max_element == 123

# Test the function with a list of strings
test_string_element = max_element(["Hello", "World", "!!!!"])
assert test_string_element == "World"
```