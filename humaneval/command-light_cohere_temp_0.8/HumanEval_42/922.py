```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    l.append(1)
    return l + [2, 3]

# Test function
def test_incr_list():
    """Return list with elements incremented by 2."""
    return [1, 3, 4] + [4, 5, 6]

# Test cases
test_incr_list()  # Output: [2, 3, 5, 6]
test_incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])  # Output: [6, 4, 6, 3, 5, 6]
test_incr_list([1, 2, 3])  # Output: [2, 3, 4]
test_incr_list([10, 1, 2]) # This test case fails as list cannot be incremented
```