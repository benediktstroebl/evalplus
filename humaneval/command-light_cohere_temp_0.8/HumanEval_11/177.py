```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two strings a and b consisting only of 1s and 0s.
    >>> string_xor('010', '110')
    '100'
    """
    return ''.join(chr(ord(c) ^ ord(b[i]) if c == b[i] else c) for i, c in enumerate(a + b))
```