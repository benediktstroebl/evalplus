```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [x + 1 for x in l]
    return new_list

# Test case 1
assert incr_list([1, 2, 3]) == [2, 3, 4]

# Test case 2
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
assert incr_list(test_list) == [6, 4, 6, 3, 4, 4, 10, 1, 124]

# Test case 3 (edge case)
test_empty = []
assert incr_list(test_empty) == []
```