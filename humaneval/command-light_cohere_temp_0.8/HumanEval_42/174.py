```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [i + 1 for i in l]
    return new_list

# Test cases
test_incr_list = [
    ("List before function", [1, 2, 3]),
    ("New list after function", [2, 3, 4]),
    ("List after multiple calls", [5, 3, 5, 2, 3, 3, 9, 0, 123])
]

# Function test
def test_function(test_case):
    try:
        result = incr_list(test_case[1])
        assert result == test_case[2]
    except AssertionError as e:
        print(f"Test case {test_case} failed: {e}")
        raise e

# Run the tests
test_incr_list = test_function(test_case)
```
The provided Python script defines a function `incr_list` that increments elements of a given list by 1 and a `test_incr_list` function that validates this function with provided test cases. The script also includes a `test_function` that uses `assert` statement with `AssertionError` to check if the `incr_list` function produces the expected results for the provided test cases. 
Finally, the `test_incr_list` function is called with the test case, and any failure is reported.