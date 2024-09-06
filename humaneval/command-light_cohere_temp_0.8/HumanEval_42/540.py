```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [x + 1 for x in l]
    return new_list

# Test the function with a list of elements
test_list = [1, 2, 3]
result = incr_list(test_list)
assert result == [2, 3, 4]

# Test the function with a list of custom elements with repeating values
test_others = [5, 3, 5, 2, 3, 3]
result = incr_list(test_others)
assert result == [6, 4, 6, 3, 4, 4]
```