```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    l.append(1)
    return l + [1]

# Test function
def test_incr_list():
    """Return list with elements decremented by 1."""
    l = [1, 2, 3]
    l.pop(1)
    return l + [0]

# Test cases
test_incr_list()
assert incr_list(l) == [1, 2, 3]
assert incr_list([1, 2, 3]) == [2, 3, 4]
assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 4, 10, 1, 124]
```