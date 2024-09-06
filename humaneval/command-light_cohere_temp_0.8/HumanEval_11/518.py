```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting only of ones. XOR returns each by concatenating ones and converting to binary.
    return ''.join(map(str.format, (bin(ord(c)) for c in a + b)))
    """
    return str(bin(ord(c) for c in map(str.format, a + b)))
```