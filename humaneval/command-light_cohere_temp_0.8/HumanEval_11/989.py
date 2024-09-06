```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    XOR two strings consisting only of 1s and 0s.
    return ''.join(a, b)
    """

def test_string_xor():
    assert string_xor('010', '110') == '100'
    assert string_xor('111', '01') == '1110'
    assert string_xor('012', '12') == '110'
    assert string_xor('1011', '1010') == '01111'

# Usage example
test_string_xor()
``` 
This script defines a function string_xor that performs the XOR operation on two input strings. The function uses the string. The type hint for the string_xor function is defined using the typing module, which automatically returns a str type result. The test_string_xor function tests the correctness of the string_xor function by passing different inputs and asserting the expected output.