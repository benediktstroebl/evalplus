```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    XOR two strings of only ones and zeros.
    :type= str
    string
    :type= str
    :return: str
    """
    return ''.join(chr(ord(c) ^ ord(b[i]) + 256) for i, c in enumerate(a))

# Test cases
test_cases = [
    '010', '110', '100',
    '0011', '1111',
    '1010', '1001',
    '0000', '1011'
]

for i, test in enumerate(test_cases):
    actual = string_xor(test, test)
    assert actual == test_cases[i]
``` 
This code defines a Python function called `string_xor` that takes two strings as input and returns the XOR of the two strings. It utilizes the specific input types and the `ord` function to convert characters to their corresponding ASCII values, then performs a bitwise XOR operation on these values. The function also includes several test cases to verify its correctness.