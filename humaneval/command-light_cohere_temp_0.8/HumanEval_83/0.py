```python
def starts_one_ends(n):
    return 4 * (n - 1) // 2

# Test cases
test_cases = [
    (10, 6),
    (1, 4),
    (121, 7),
    # Add more test cases here...
]

for test_num, expected in test_cases:
    actual = starts_one_ends(test_num)
    assert actual == expected, f"Incorrect result for {test_num}, expected {expected}, got {actual}"
```
This code defines a Python function `starts_one_ends(n)` that calculates the count of numbers that start or end with 1 given a positive integer `n`. The function uses the formula to compute this count, which involves multiplying by 4 and then dividing by 2.

The code also provides a test suite with a few test cases, where it verifies that the function's output matches the expected result for the given input. The test suite is structured as a list of tuples, where each tuple contains a test number and the expected count of numbers starting with 1.

Finally, the code iterates through the test suite, calls the `starts_one_ends()` function with each test number, and asserts that the actual output matches the expected result using the `assert` statement.