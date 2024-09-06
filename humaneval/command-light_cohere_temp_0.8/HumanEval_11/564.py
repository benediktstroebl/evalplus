```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting of only ones and zeros
    O(n) time complexity"""
    return ''.join(chr(ord(a[i]) ^ ord(b[i])) for i in range(len(a)))

# Test cases
string_xor('010', '110')
#100
string_xor('111', '000')
#101
string_xor('00111', '1010')
#011
string_xor('1010', '1010')
#0
```