```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    l.append(1)
    return l + [1]

# Test case 1
test_incr_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_incr_list_expected = [6, 4, 6, 3, 4, 4, 10, 1, 124]

# Test case 2
test_incr_list2 = [5, 3, 5, 2, 3]
test_incr_list2_expected = [6, 4, 6]

def test_incr_list(test_case):
    test_incr_list = incr_list(test_case)
    print("Test case:", test_incr_list_expected, " ====" , test_incr_list)

# Run the tests
test_incr_list(test_case1)
test_incr_list(test_case2)
```

This Python script defines a function `incr_list` that adds one to the end of an input list, and tests this function using two test cases.  It creates a test cases, which pass to the `test_incr_list` function and expect the results to match the expected output.