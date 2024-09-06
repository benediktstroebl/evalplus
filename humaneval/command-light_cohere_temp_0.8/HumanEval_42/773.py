```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [x + 1 for x in l] + [n]
    return result

# Test cases
test_incr_list = [
    [1, 2, 3],
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [None, 10, 11, 12],
]

for test_case in test_incr_list:
    actual = incr_list(test_case)
    expected = [6, 4, 6, 3, 4, 4, 10, 1, 124]
    assert actual == expected, "Test case {} failed.".
```