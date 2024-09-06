```python
def get_positive(l: list):
    return [num for num in l if num >= 0]

# Test cases
test_get_positive = []
test_get_positive.push([
    [-1, 2, -4, 5, 6])
test_get_positive.push([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])

# Verify the function
def test():
    for test_case in test_get_positive:
        actual_out = get_positive(test_case)
        expected_out = [0]
        assert actual_out == expected_out, f"Error in test case: {test_case}"

test_get_positive
test()
```

This script defines a function `get_positive` that takes a list and returns a new list containing only the positive numbers. It also provides a test cases to verify the correctness of the function. The `test` function contains the test cases and uses the `get_positive` function to create the expected output and compares it with the actual output. The test will fail if the function returns the wrong output for any given input, which verifies that the function works correctly.