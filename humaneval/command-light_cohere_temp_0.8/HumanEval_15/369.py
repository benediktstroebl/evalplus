Here is a Python script with a self-contained function that solves the problem of generating a string of numbers from 0 to n:
```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space-delimited numbers starting from 0 and ending at n.
    if n < 0:
        return '0'
    else:
        # Use recursion to generate sequence
        return f"{0} {string_sequence(n - 1)} {n}"

# Test cases
test_cases = [0, 5, 10, 15, 20]

for test_num in test_cases:
    actual_output = string_sequence(test_num)
    assert actual_output == f"0 {test_num} {test_num + 1} n"
```
This script defines a function string_sequence that takes an integer n as input and returns a string containing space-separated numbers from 0 to n. It uses a recursive approach with the base case being when n is 0, which returns '0'. The assert statement checks if the actual output matches the expected output. This self- necessary, test cases and the results are validated against the expected output.