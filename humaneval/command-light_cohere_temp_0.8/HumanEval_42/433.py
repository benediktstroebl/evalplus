```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    new_list = [x + 1 for x in l]
    return new_list

# Test the function with a list of elements
test_list = [1, 2, 3]
result = incr_list(test_list)
assert len(result) == 3, "Length of the result is not 3"
assert all([x + 1 for x in result]) == [2, 3, 4], "The list was not properly incremented"
```