```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    return [i+1 for i in l]

# Test suite for incr_list function
def test_incr_list():
    tests = [
        [1, 2, 3],
        [5, 3, 5, 2, 3, 3, 9, 0, 123],
        [123, 456]
    ]

    for test_set in tests:
        expected = [i+1 for i in test_set]
        got = incr_list(test_set)
        assert expected == got, "Test {} failed".

# Call the test suite
test_incr_list()
```

The code defines a function `incr_list` that adds 1 to each element of the input list and returns the updated list. The `test_incr_list` function contains a series of test cases that are run against the `incr_list` function to verify its correctness. The code uses the test cases to ensure that the `incr_list` function works as expected and produces the correct results.