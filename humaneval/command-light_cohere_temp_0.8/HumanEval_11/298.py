```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Inputs are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    return ("".join_map("1" if c == "0" else "0" for c in a ^ b))

# Test suite
def test_string_xor():
    assert string_xor("010", "110") == "100"
    assert string_xor("1111", "0110") == "1010"
    assert string_xor("1010", "1010") == "1000"
    assert string_xor("000", "00") == "0000"
    assert string_xor("111", "01") == "10"
    assert string_xor("1010", "1101") == "1110"
    assert string_xor("0011", "1111") == "0000"

if __name__ == "__main__":
    test_string_xor()
``` 
This code defines a function `string_xor` that performs a bitwise XOR operation on two input strings consisting of only ones. It then passes the orange for inputs, and returns the result as a string. This function is the then be useful for any string inputs that follow this pattern.