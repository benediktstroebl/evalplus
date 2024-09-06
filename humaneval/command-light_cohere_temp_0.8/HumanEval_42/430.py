```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [x + 1 for x in l]
    assert len(result) == n, f"List length mismatch: {len(result)} != {n}"
    return result

# Test suite
def test_incr_list():
    tests = [
        [([1, 2, 3], [2, 3, 4]),
        ([5, 3, 5], [6, 4, 6]),
        ([10, 9, 0], [10, 1, 2, 3]),
        ([123, 0, 123], [124, 1, 2, 3])],
    ] + [[(x, y) for x, y in zip(a, b)] for a, b in tests])
    for test, expected in tests:
        actual = incr_list(test)
        print(f"Test: {actual}, {expected}")
        assert actual == expected, f"Failed test: {test}"

# Main
if __name__ == "__main__":
    test_incr_list()
```
The provided Python script defines a function `incr_list` that takes a list as input and returns a new list with elements incremented by 1. The `test_incr_list` function contains a series of test cases with different lists and expected results. 

This script also follows the concept of self-containment and can be executed directly to run the full test suite and display the results.