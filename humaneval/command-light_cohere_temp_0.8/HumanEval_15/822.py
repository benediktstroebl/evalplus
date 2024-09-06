Here is a Python script with a self-contained function that solves the problem of generating a string of numbers from 0 to n:
```python
def string_sequence(n: int) -> str:
    return "".join(str(i) for i in range(0, n+1))

# Test cases
test_cases = [
    (0, ""),
    (5, '0 5'),
    (10, '0 9 10'),
    # Bigger numbers and custom separator
    (5, '123 456 789 123'),
]

# Function for testing the function
def test_function(func, test_cases):
    for case, expected in test_cases:
        got = func(case)
        assert got == expected, f"Failed for {case}, expected {expected}, got {got}"

# Run the tests
test_function(string_sequence, test_cases)
```

This script defines a function called string_sequence that generates a string of numbers from 0 up to a given integer n. The function then defines a corresponding test cases and a function to run the tests. Finally, it runs the test_function with the defined test cases, which should pass if the function is working correctly.