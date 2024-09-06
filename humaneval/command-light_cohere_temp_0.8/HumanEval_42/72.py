```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    l.append(1)
    return l + [0]

# Test function
def test_incr_list():
    """Return list with elements decremented by 1"""
    l = [0]
    l.append(1)
    return l + [1]

# Test cases
tests = [test_incr_list.assert_equal(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]), [[6, 4, 6, 3, 4, 4, 4, 10, 1, 124]])

# Run the function and tests
result = incr_list(tests)
result. assert_equal(result, tests)
```

This script defines a function `incr_list` that adds 1 to the last element of the passed list and then returns a new list with the incremented elements. The `test_incr_list` function is a test function that returns a list with elements decremented by 1 and passes the test by comparing the result with the expected output from `incr_list`.  The script then creates a list of test cases and runs the `incr_list` function and tests, passing the `tests` argument.  The expected output will the same list with elements decremented by 1.