```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two input strings a and b consisting only of digits 1 or 0.
    """
    string XOR(a, b) = a ^ b 
    """
    return ''.join(a ^ b)

# Test suite
def test_string_xor():
    assert string_xor('010', '110') == '100'
    assert string_xor('111', '010') == '001'
    assert string_xor('000', '111') == '111'
    assert string_xor('1', '01') == '11'
    assert string_xor('1000', '001') == '1001'

if __name__ == "__main__":
    test_string_xor()
```
The code defines a function `string_xor` that XORs two input strings, consisting only of digits 1 or 0. The test suite contains a set of test cases that validate the correctness of the `string_xor` function. 

This code is self-contained and does not require any external modules or functions.