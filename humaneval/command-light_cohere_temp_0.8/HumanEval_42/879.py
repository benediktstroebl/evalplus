```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_elements = [x + 1 for x in l]
    return new_elements

# Test the function with a list of elements
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result = incr_list(test_list)

# Print the result
print(result)

# Test the function with a tuple of elements
test_tuple = (5, 3, 5, 2, 3, 3, 9, 0, 123)
result_tuple = incr_list(test_tuple)

# Print the result
print(result_tuple)
```