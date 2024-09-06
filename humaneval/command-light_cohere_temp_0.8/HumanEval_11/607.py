```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting only of ones and zeros.
    A: '101010'
    B: '0101010'
    """
    assert len(a) == len(b)
    assert all(c == '0' if c == '0' else c == '1' for c in a)
    assert all(c == '0' if c == '0' else c == '1' for c in b)
    assert a[0] == '1' and a[1] == '0'
    assert b[0] == '0' and b[1] == '1'
    return a ^ b
```