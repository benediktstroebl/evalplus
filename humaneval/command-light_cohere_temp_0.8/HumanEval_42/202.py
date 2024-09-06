```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [x + 1 for x in l]
    return new_list

# Test function to check the correctness of incr_list function
def test_incr_list():
    test_list = [1, 2, 3]
    result = incr_list(test_list)
    expected = [2, 3, 4]
    assert result == expected, "Test 1 failed"

    test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    result = incr_list(test_list)
    expected = [6, 4, 6, 3, 4, 4, 10, 1, 124]
    assert result == expected, "Test 2 failed"

# Main function to call the function with a test list
test_incr_list()
```
This Python code provides a self-contained function `incr_list` that efficiently generates a new list with elements incremented by 1. It also includes a test function to validate the correctness of the `incr_list` function using a test list and asserting the expected results match the actual results. 

The `main` function serves to execute the `test_incr_list` function with a test list, which ensures the function's expected behavior is correctly implemented.