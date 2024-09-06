```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [x + 1 for x in l]
    return new_list

# Test the function with different inputs
# Expected output: [2, 3, 4]
test_incr_list = [1, 2, 3]
result = incr_list(test_incr_list)
assert result == [2, 3, 4]

# Test with different lengths
# Expected output: []
test_empty_list = []
result = incr_list(test_empty_list)
assert result == []

# Test with nested list
# Expected output: [6, 4]
test_list_with_nested = [5, 3, 5, 2, 3, 3]
result = incr_list(test_list_with_nested)
assert result == [6, 4]

# Test with different values in a list
# Expected output: [10, 1, 124]
test_dynamic = [0, 123]
result = incr_list(test_dynamic)
assert result == [10, 1, 124]
```
This code defines a function incr_list that takes a list l as input and returns a new list with elements from the original list incremented by 1. The test section includes several tests to verify the correctness of the incr_list function.