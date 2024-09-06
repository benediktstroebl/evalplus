```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    l.append(1)
    return l + [0, ]

# Test suite
def test_incr_list():
    tests = [
        [1, 2, 3],
        [5, 3, 5, 2, 3, 3, 9, 0, 123],
        [100, 3, 100, 2, 3, 3, 999, 0, 1234],
    ]

    for test in tests:
        expected = [test + 1]
        actual = incr_list(test)
        assert expected == actual, f"Test {test} failed"

test_incr_list()
```