```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [x + 1 for x in l]
    return new_list

# Test the function with different inputs
# Test with list filled with integers
test_incr_list = [1, 2, 3]
result = incr_list(test_incr_list)
assert result == [2, 3, 4]

# Test with different types of data
test_mixed = ['a', (5), 'b', (3, 2)]
result = incr_list(test_mixed)
assert result == ['a', 6, 'b', 6]

# Test with empty list
test_empty = []
result = incr_list(test_empty)
assert result == []

# Test with a nested list
test_nested = [[1, 2, 3], [4, 5, 6]]
result = incr_list(test_nested)
assert result == [1, 3, 5, 8]
```
This script defines a function `incr_list` that takes a list as input and returns a new list with elements incremented by 1. The test cases cover various scenarios: basic integer lists, mixed data types, empty lists, and nested lists. 

The output of the function is then compared against the expected results from each test case using `assert`.