```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [i + 1 for i in l] + l
    return result

# Test function
def test_incr_list():
    assert incr_list([1, 2, 3]) == [2, 3, 4]

# Test with nested lists
assert incr_list([5, 3, 5, 2, 3, 3]) == [6, 4, 6, 3, 4, 4]

# Test with varying lengths
assert incr_list([5, 3]) == [6, 3]
assert incr_list([]) == []
assert incr_list([1, 2, 3, 4, 5]) == [2, 3, 4]
```