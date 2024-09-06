```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [x + 1 for x in l]
    assert len(result) == n
    assert all(result) == l + [0]
    return result

# Test suite
def test_incr_list():
    tests = [
        [([1, 2, 3], [2, 3, 4]),
        ([5, 3, 5], [6, 4, 6]),
        ([], [0])
    ]
    )
    for test, expected in tests:
        actual = incr_list(test)
        assert actual == expected, f"Test '{test}' failed."

# Example usage
test_incr_list()
```
This Python code defines a function `incr_list` that returns a new list with elements from an input list incremented by 1. It also includes a test suite, which contains three test cases to verify the correctness of the `incr_list` function. The function's assertions check that the length of the result list matches the input list's length and that the result list is the same as the input list plus a zero element.