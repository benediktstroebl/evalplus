```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    XOR two strings, a and b, consisting only of 1s and 0s.
    """
    time a strings are split into lists of 1s and 0s
    a:list = [int(c) for c in a]
    b:list = [int(c) for c in b]
    return ''.join(str(a ^ b))
    """

def test_string_xor():
    """
    Test string_xor function with some inputs.
    assert string_xor('010', '110') == '100'
    assert string_xor('abc', '123') == '234'
    assert string_xor('abc', '0') == '240'
    assert string_xor('111', '1') == '201'
    assert string_xor('', '') == ''
    assert string_xor('', '1') == '001'
    assert string_xor('abc', 102) == '102'
    assert string_xor('01', '10') == '110'
    assert string_xor('111', '111') == '000'
```
This code includes a function that performs the XOR operation on two strings consisting only of ones, and another function to test the correctness of the XOR function with various inputs.