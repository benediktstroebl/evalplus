```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two strings, a and b, consisting only of ascii 1s and 0s.
    Return the string concatenation of the two inputs in reverse order and perform XOR.
    Return the string concatenation of the two inputs in reverse order and perform XOR.
    """
    string_xor('110', '010')
    """
    # reverse strings
    b_rev = b[::-1]
    a_rev = a[::-1]
    # xor the strings
    result = a_rev ^ b_rev
    return result
```