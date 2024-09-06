```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    res = [x + 1 for x in l]
    return res

# Test suite
def test_incr_list():
    test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    expected = [6, 4, 6, 3, 4, 4, 10, 1, 124]
    assert list(incr_list(test_list)) == expected, "Test 1 failed"
    test_list = [1, 2, 3]
    expected = [2, 3, 4]
    assert list(incr_list(test_list)) == expected, "Test 2 failed"
    test_list = [5]
    expected = [6]
    assert list(incr_list(test_list)) == expected, "Test 3 failed"

if __name__ == "__main__":
    test_incr_list()
```
The Python code defines a function `incr_list` that increments elements of a given list by 1 and returns the modified list. The function is then tested with three different input lists using the `test_incr_list` function, which contains various test cases. The test suite ensures that the function operates correctly for different scenarios of input lists.