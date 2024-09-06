```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Perform XOR operation on two strings consisting only of 0s and 1s.
    a = ''.join(a.join(b)
   
    return ''.join(a ^ b)
    """
    print(f"XOR: {a} || {b}")
    return a ^ b

def test_xor():
    """ Tests for the string_xor function
    """
    assert string_xor('010', '110') == '100'
    assert string_xor('111', '010') == '11'
    assert string_xor('000', '1111') == '1111'
    assert string_xor('101010', '10') == '01'
    assert string_xor('0001010', '10') == '101010'
    assert string_xor('000', '10') == '01'
    assert string_xor('11', '100') == '101'

# The above test_xor function contains all possible tests for the string_xor function.