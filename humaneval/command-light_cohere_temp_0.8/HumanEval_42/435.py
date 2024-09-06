```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [x + 1 for x in l]
    return new_list

# Test the function with various inputs
test_incr_list = incr_list.__code__
test_incr_list([1, 2, 3])
test_incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
test_incr_list([])
test_incr_list([10])
test_incr_list([1, 2, 3, 4, 5, 6])
```