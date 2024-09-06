```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    XOR two strings consisting only of ones and zeros
    """
    return "".join(c ^ int(a[i]) for i, c in enumerate(b))

# Test cases for function
def test_xor():
    assert string_xor("010", "110") == "100"
    assert string_xor("1100", "0011") == "1110"
    assert string_xor("abcdef", "012") == "10acdef"
    assert string_xor("", "") == ""

# Run tests
test_xor()
``` 
This Python script defines a function called `string_xor` that performs the XOR operation on two strings, which only contain ones and zeros. It uses a `enumer other characters in the second string to perform the operation, and returns the result as a string.