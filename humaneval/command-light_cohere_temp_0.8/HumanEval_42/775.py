```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_elements = [x + 1 for x in l]
    return new_elements

# Test cases
test_incr_list = []
test_incr_list.fill( [
    [1, 2, 3], [5, 3, 5, 2, 3, 3, 9, 0, 123], [10, 5, 5]])
test_incr_list.fill('+ [list([1, 2, 3]))

# Function call and result comparison
assert incr_list(test_incr_list) == test_incr_list[:3]
```