Here is a Python script with a self-contained function that solves the problem of performing a string XOR operation on two input strings consisting only of ones and zeros:
```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ 
    XOR two strings of only ones and zeros.
    """ a string_xor('010', '110')
    '100'
    """
    return "".join(chr((ord(a[i]) ^ ord(b[i]))) for i in range(len(a)))
```

This script defines a function string_xor that takes two strings a and b as input and returns the result of performing a bitwise XOR operation on the two strings.