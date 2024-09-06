```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform XOR operation on two input strings composed of only digits 1 and 0.
    """
   
    return a string obtained by performing bitwise XOR operation on each character of a and b.
    """
    tests if the string_xor('101010', '0101010')
    assert True
    assert string_xor('101010', '0101010') == '01011010'
    assert string_xor('101010', '011010') == '01101010'
    assert string_xor('000101', '11000101') == '0011000101'
    assert string_xor('10101010', '10101010') == '0110101010'
    assert string_xor('10101010', '0110101010') == '101010101010'
    assert string_xor('10101010', '11101010101') == '1110101010101'
    assert string_xor('0001101', '0001101') == '00000110110011011011011'
    assert string_xor('1010', '0001101') == '0001101'
    assert string_xor('1010', '0001010') == '00011010'
    assert string_xor('1010', '1010') == '1010'
    assert string_xor('1010', '11') == '1111'
    assert string_xor('110', '010') == '011'
    assert string_xor('000', '') == '0'
    assert string_xor('', '') == ''
```