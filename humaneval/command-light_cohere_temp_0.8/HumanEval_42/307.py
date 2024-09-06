```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [x + 1 for x in l]
    return new_list

# Test cases
test_incr_list = [
    ("Input: [5, 3, 5, 2, 3, 3, 9, 0, 123]")
    (
        "Expected Output: ([6, 3, 6, 4, 6, 4, 4, 10, 1, 124]\n"
        "got: [5, 3, 5, 3, 4, 5, 9, 7, 123]"
    ),
    (
        "Input: [1, 2, 3, 4] -> [[2, 3, 4, 5, 6, 7, 8, 9]"
    )
]

# Function call and test results
for test_case in test_incr_list:
    print("---", end="")
    print(test_case[0])
    print(f"Expected Output: { coalesce([{**test_case[1]}]) }")
    print(f"Got: {coalesce([{**test_case[2]}])}")
    assert_equal(test_case[2], test_case[1])
    print("pass")
```

This Python script defines a function `incr_list` that returns a new list with elements incremented by 1. The test cases provide input lists and expected output lists, and the `assert_equal` function is used to verify the results against the expected output.

The script then iterates through the test cases and prints the input and expected output before comparing the actual output with the expected output, using `assert_equal`. Finally, it prints "pass" to indicate successful test execution.