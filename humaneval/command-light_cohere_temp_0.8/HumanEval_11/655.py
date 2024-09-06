```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Perform XOR operation on two strings a and b consisting only of 1s and 0s
    and return the result as a string.
    >>> string_xor('010', '110')
    '100'
    >>> string_xor('00', '01')
    '01'
    >>> string_xor('111', '1')
    '11'
    >>> string_xor('', '')
    '0'
    >>> string_xor('abcdefgh', '012')
    'defgh'
    >>> string_xor('bit', 'b')
    'abit'
    """
    if len(set(a)) != 2 or len(set(b)) != 2:
        raise ValueError("Input strings must contain only the digit 1")
    return ''.join(chr((ord(a[i]) ^ ord(b[i]))) for i in range(len(a)))
```