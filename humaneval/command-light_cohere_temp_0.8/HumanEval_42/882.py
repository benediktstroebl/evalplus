```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [i+1 for i in l]
    assert len(result) == n
    assert all(result[i] == i+1 for i in range(n))
    return result

# Test code
# Test list with single element
test_incr_list([1])
result = incr_list([1])
assert result == [2]

# Test list with multiple elements
test_incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
result = incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
assert result == [6, 4, 6, 3, 4, 4, 10, 1, 124]

# Test list with custom element
test_incr_list([None])
result = incr_list([None])
assert result == [1]

# Test list with negative increment
test_incr_list([1, -5])
result = incr_list([1, -5])
assert result == [0, -6]
```