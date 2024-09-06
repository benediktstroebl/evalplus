```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two strings consisting of only '1' and '0'.
    """
    # Use built-in string XOR
    return ''.join(c ^ d for c, d in zip(a, b))

# Test cases
test_cases = [
    '010', '110', '100',
    '001', '101', '110',
    '0000', '1111'
]

# Function Test
def test_string_xor():
    for case in test_cases:
        assert string_xor(case, case) == '0000'

# Run tests
test_string_xor()
```
This Python script provides a self-contained function `string_xor` that performs the XOR operation on two strings consisting of only '1' and '0', and returns the result as a string. It also includes a test cases and a test function to verify the correctness of the `string_xor` function against the test cases.  The test_cases include various strings with distinct patterns, and the `test_string_xor` function checks if the function correctly performs the XOR operation for each pair of input strings.