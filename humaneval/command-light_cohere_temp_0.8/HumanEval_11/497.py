```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two input strings.
    >>> string_xor('010', '110')
    '100'
    """
    return str(bin(ord(a[0]) ^ ord(b[0]))[2:])
```