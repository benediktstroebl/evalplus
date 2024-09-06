```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    XOR two strings consisting only of 1s and 0s.
    >>> string_xor('010', '110')
    '100'
    """
    return str(bin(ord(a[0]) ^ ord(b[0]))[2:])

# test suite
strings = [
    '010', '110', '100',
    '0011', '1001', '1010'
]

for s in strings:
    got = string_xor(s, s)
    assert got == s
    assert len(got) == 6
```