```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Perform XOR operation on two strings consisting only of 1s and 0s.
    >>> str_list = ['010', '110', '0011', '0110', '0000']
    >>> string_xor('', '')
    Traceback (most recent call last):
    ...
    ValueError: 'a' and 'b' must contain only single characters: ['', '']
    >>> string_xor('abc', '123')
    Traceback (most recent call last):
    ...
    ValueError: 'a' and 'b' must contain only single characters: ['abc', '123']
    >>> string_xor('111', '01')
    Traceback (most recent call last):
    ...
    ValueError: 'a' and 'b' must contain only single characters: ['111', '01']
    >>> string_xor('01111', '000')
    '1111'
    >>> string_xor('00', '1111')
    '1111'
    >>> string_xor('111', '1110')
    '01'
    >>> string_xor('000', '00')
    '000'
    >>> string_xor('01', '1010')
    '1010'
```