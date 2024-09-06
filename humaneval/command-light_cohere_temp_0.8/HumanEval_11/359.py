```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform binary XOR operation on two strings a and b and return the result as a string.
    Args:
        a: str, First string to perform XOR operation.
        b: str, Second string to perform XOR operation.
    Returns: XOR(a, b) and return the result.
    """ xor(a) = a ^ b
    xor = int('1') << (ord(a[0]) - ord(b[0]))
    return chr(xor)
    return xor
```