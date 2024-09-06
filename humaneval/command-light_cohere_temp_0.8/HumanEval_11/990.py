```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two strings with only ones and zeros.
    Returns: bitwise representation of both strings and performs xor operation.
    """.
    return result as a + string of the bits of the result.
    """.

    Test input strings awords, '010' and '110', perform the xor
    operation and return the result as the string '100'. 
def test_string_xor():
    """ Test the string_xor function
    """
    assert string_xor('010', '110') == '100'
    assert string_xor('111', '110') == '0'
    assert string_xor('100', '0') == '0'
    assert string_xor('0000', '1111') == '1111'
    assert string_xor('777', '888') == '5555'
    assert string_xor('1234', '5678') == '12357'
    assert string_xor(' ', ' ') == ' '
    assert string_xor('abc', 'cba') == 'abcba'
    assert string_xor('00', '11') == '1100'
```