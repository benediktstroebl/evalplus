```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    l.append(l[-1] + 1)
    return l

# Test function
def test_incr_list():
    assert list(incr_list([1, 2, 3]) == [2, 3, 4])

# Test case with nested list
assert list(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])) == [6, 4, 6, 3, 4, 4, 4, 10, 1, 124]

# Test with custom data type (list)
test_incr_list()
```