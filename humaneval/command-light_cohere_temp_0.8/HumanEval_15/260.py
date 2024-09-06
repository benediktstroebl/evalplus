```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n+1)

# Test cases for function
test_string_sequence = [
    (0, "0"),
    (1, "1"),
    (5, "0 5 10 15 20"),
    (6, "0 1 2 3 4 5 6")
]

# Function to run the tests
def test_function(test_case): 
    assert test_case[0] == test_string_sequence(test_case[1])

# Run the tests
test_function(test_case)
``` 
This script defines a function `string_sequence` which returns a string with numbers separated by spaces, starting from 0 and ending at `n` (inclusive). It also defines a test suite `test_string_sequence` with different test cases to verify the function's correctness.  The then the test_function takes a test case as input and asserts that the corresponding output of `string_sequence` function matches the expected value.