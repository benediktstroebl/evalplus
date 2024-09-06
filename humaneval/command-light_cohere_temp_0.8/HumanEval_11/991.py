```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting only of digits 1 and 0.
    Returns the different string of the digits in the order of first input.
    >>> string_xor('010', '110')
    '100'
    """
    return "".join(ord(c) ^ ord(d) for c, d in zip(a, b))

#Test cases
def test_string_xor():
    assert string_xor('010', '110') == '100'
    assert string_xor('0011', '1111') == '0000'
    assert string_xor('001', '01') == '001'
    assert string_xor('000', '1111') == '1111'
    assert string_xor('1234', '5') == '2345'
    assert string_xor('', '') == ''
```