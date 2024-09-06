Here is a Python script with a self-contained function that solves the problem of XORing two strings:
```python
# Function to perform XOR of two strings
def string_xor(a: str, b: str) -> str:
    return a ^ b  # return the result of string concatenation using operator '^'

# Test cases for the function
tests = [
    ("010", "110")  # Tests if XOR works correctly for 1s and 0s
    ("abc", "cba")  # Tests if XOR works correctly for all characters
    ("\n", "")  # Tests if XOR works correctly for empty strings
]

for case in tests:
    actual = string_xor(case[0], case[1])
    assert actual == case[2], f"Error in test case {case}"
```
The function performs a simple XOR operation on the two input strings, which are assumed to contain only the characters '0' and '1'.