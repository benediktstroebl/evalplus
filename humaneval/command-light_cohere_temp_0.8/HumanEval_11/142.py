```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two input strings consisting only of '1' and '0' characters.
    """
    result = a sum([ord(c) ^ ord(b) for c in a])
    return str(result)

# Test cases
test_cases = [
    ("010", "110"),
    ("001", "101"),
    ("1010", "01"),
    ("000", "100"),
    ("1111", "1111")
]

# Function calls
for tc in test_cases:
    print(tc[0] ^ tc[1]) == tc[2]  # Expected output is also printed
``` 
This code defines a function called `string_xor` that performs the XOR operation on two input strings, consisting only of the characters '1' and '0'. The function uses the built-in `ord` function to get the ASCII value of each character, and then performs a bitwise XOR operation on these values. 
This is a common and efficient way to perform an XOR operation on strings of characters in the range '01'.