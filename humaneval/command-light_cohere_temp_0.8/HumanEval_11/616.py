```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting only of 1s and 0s.
    Converts inputs to lists of characters, then returns list's XOR.
    >>> string_xor('010', '110')
    '100'
    """
    return ''.join([c ^ b.pop(ord(c)) for c in a] ^ [c ^ b.pop(ord(c)) for c in b])
```