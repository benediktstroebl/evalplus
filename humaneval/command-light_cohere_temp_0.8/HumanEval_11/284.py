```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    Inputs are two strings a and b consisting only of 1s and 0s.
    Returns binary XOR operation and returns a string.
    """
    XOR(b) = a ^ b
    """
    return str(XOR(b))

def XOR(a: int) -> str:
    """ Conversion of 32-bit integers to binary string"""
    return bin(a)[2:]

# Test case
def test_string_xor():
    assert string_xor("010", "110") == "100"

test_string_xor()
``` 
This script defines a function `string_xor` that performs the XOR operation on two input strings, which only contain characters '0' and '1'. The `XOR` function takes a 32-bit binary string as input and returns the corresponding string.