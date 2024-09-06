```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two strings consisting of only digits 1 and 0.
    """
    Input is two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on this inputs and return result also as a string.
    """
    XOR(x, y) = x ^ y
    """
    return ''.join(str(i) for i in [a ^ b, b ^ a])
```