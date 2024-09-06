```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    l.append(l[0] + 1)
    return l

# Test suite
def test_incr_list():
    test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    expected = [6, 4, 6, 3, 4, 4, 10, 1, 124]
    for test, expected in zip(test_list, expected):
        actual = incr_list(test)
        assert actual == expected, f"Failed for {test} expected {expected}, actual {actual}"

# Test initial value
test_list = [5, 3, 5, 2, 3, 3]
actual = incr_list(test_list)
assert actual == [6, 4, 6, 3, 4, 4, 10], "Failed for initial value"

# Test list with repeated values
test_list = [5, 3, 5, 2, 3, 3, 3, 9, 0, 123]
expected = [6, 4, 6, 3, 4, 4, 6, 3, 124]
assert actual == expected, "Failed for repeated values"

# Test empty list
test_list = []
actual = incr_list(test_list)
assert actual == [], "Failed for empty list"

test_incr_list()
```