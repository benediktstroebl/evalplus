```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [x + 1 for x in l]
    return new_list

# Test the function with known good inputs/outputs
test_incr_list = lambda: [1, 2, 3] == incr_list([1, 2, 3]) and [5, 3, 5, 2, 3, 3, 9, 0, 123] == incr_list([5, 3, 5, 2, 3, 3, 3, 9, 0, 123])
```