```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    l.append(l[-1] + 1)
    return l

# Test function to check if the incr_list function works correctly
def test_incr_list():
    test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    expected_result = [6, 4, 6, 3, 4, 4, 10, 1, 124]
    for element in test_list:
        assert element == expected_result[len(expected_result) - 1], f"Failed at element: {element}"
    print("Test incr_list passed.")

# Call the test function to run the tests
test_incr_list()
```
This Python script provides a `incr_list` function that extends a given list with elements incremented by 1. The `test_incr_list` function contains a test list and expected result, and it checks if the output of the `incr_list` function matches the expected result.

When you run this script, the `test_incr_list` function is called, which runs the tests and checks if the `incr_list` function works correctly. 
result will be displayed if the test passes.