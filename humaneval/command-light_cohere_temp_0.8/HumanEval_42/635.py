```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [x + 1 for x in l]
    return new_list

# Test case 1
assert incr_list([1, 2, 3]) == [2, 3, 4]

# Test case 2
assert incr_list([5, 3, 5]) == [6, 5, 6]

# Test case 3
assert incr_list([9, 0, 123]) == [10, 0, 124]
```