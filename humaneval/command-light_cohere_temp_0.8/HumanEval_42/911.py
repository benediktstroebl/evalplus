```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [i + 1 for i in l]
    return new_list

# Test function
def test_incr_list():
    input_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    result = incr_list(input_list)
    expected_result = [6, 4, 6, 3, 4, 4, 10, 1, 124]
    assert result == expected_result, "Test failed: actual != expected"

# Run the test and show the results
print("Test results:")
test_incr_list()
print()
```
The function incr_list generates a new list with elements incremented by 1. The test_incr_list function provides a unit test with a sample input list and expected result. The test function uses the dry run and asserts that the result matches the expected output. The output shows the results of running the test.

This Python code defines a function to increment lists by 1 and passes an automated test using the assert statement. The test is performed using the input list provided in the test_incr_list function.