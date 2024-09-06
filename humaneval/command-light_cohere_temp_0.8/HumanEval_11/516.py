```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting of only ones and zeros.
    >>> str_xor('010', '110')
    '100'
    >>> str_xor('00', '00')
    '0000'
    >>> str_xor('00', '01')
    '01'
    >>> str_xor('000', '0000')
    '000'
    >>> str_xor('000', '111111')
    '111111'
    """
    return a ^ b
```