```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two strings of only ones and zeros
    """
    # Convert to list of characters to perform XOR
    a = ''.join(a)
    b = ''.join(b)
    return ''.join(a XOR b)

# Test
test_cases = [
    "010",
    "110",
    "0011",
    "1010",
    # Add more tests here...
]

for test_case in test_cases:
    result = string_xor(*test_case)
    assert result == test_case[0] + test_case[1]
``` 
This code defines a function named `string_xor` that performs a bitwise XOR operation between two input strings, consisting only of the characters '0' and '1'. The function takes two string arguments and returns the XOR of the two strings, which is also a string.

The `test_cases` variable holds a list of test cases, where each test case is a pair of two strings. This variable is tested to test the `string_xor` function with each test case and verifies if the result matches the expected output of the XOR operation.