```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [i + 1 for i in l]
    return new_list

# Test case 1: Basic increment
assert list(incr_list([1, 2, 3])), [2, 3, 4]

# Test case 2: Existing element at front
assert list(incr_list([5, 3, 5, 2, 3, 3])), [6, 4, 6, 3, 4]

# Test case 3: Existing element at middle
assert list(incr_list([5, 3, 5, 2, 3, 3])), [6, 4, 6, 3, 4]

# Test case 4: Existing element at end
assert list(incr_list([9, 0, 123])), [10, 1, 124]

# Test case 5: Empty list
assert list(incr_list([])), []
```