```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [x + 1 for x in l]
    return new_list

# Test the function with a list of values
test_list = [1, 2, 3]
test_result = incr_list(test_list)
assert test_result == [2, 3, 4]

# Test the function with a list of complex values
test_values = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_result = incr_list(test_values)
assert test_result == [6, 4, 6, 3, 4, 4, 10, 1, 124]
```
The function incr_list takes a list l as input and returns a new list with elements from the original list incremented by 1. This is is used to test the function's correctness with the test cases provided.