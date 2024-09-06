```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [i+1 for i in l] + l
    assert len(result) == n + 1, f"Unexpected length {len(result)}, expected {n+1}"
    return result

# Test suite
def test_incr_list():
    tests = [
        ([1, 2, 3], [5, 3, 5, 2, 3, 3, 9, 0, 123])
    ]
    for test, expected in tests:
        actual = incr_list(test)
        assert actual == expected, f"Test {test} failed: {actual} != {expected}"

# Example usage
test_incr_list()
```