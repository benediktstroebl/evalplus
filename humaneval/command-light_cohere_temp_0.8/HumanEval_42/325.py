```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [x + 1 for x in l]
    return new_list

# Test the function with a list of integers
test_incr_list = [1, 2, 3]
result = incr_list(test_incr_list)
assert result == [2, 3, 4]

# Test the function with nested list
test_nested = [5, 3, 5, 2, 3, 3]
result_nested = incr_list(test_nested)
assert result_nested == [6, 4, 6, 3, 4, 4]

# Test the function with complex list
test_complex = [0, 123, 9, 1]
result_complex = incr_list(test_complex)
assert result_complex == [6, 124, 6, 10, 1]
```
The Python code defines a function `incr_list` that incrementally element in a list by 1. The function takes a `l` as input and returns a new list with elements incremented by 1. The code then creates a test functions to verify the correctness of the `incr_list` function with different types of lists. 

This code follows the PEP 8 style guidelines and is a good starting point for writing efficient and clean Python code.