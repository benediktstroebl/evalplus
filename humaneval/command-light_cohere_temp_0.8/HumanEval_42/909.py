```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [x + 1 for x in l]
    return new_list

# Test the function with a list of integers
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result = incr_list(test_list)

# Check if both input and output lists are equal
print(test_list == result)
```