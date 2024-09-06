```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform binary XOR operation on two strings consisting only of 1s and 0s.
    >>> string_xor('010', '110')
    '100'
    """
    return ''.join(chr(255 - (ord(c) ^ ord(b[i]))) for i, c in enumerate(a))
```