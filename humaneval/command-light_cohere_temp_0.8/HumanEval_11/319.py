```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two input strings using bitwise operations
    """
    return ''.join(chr((ord(a[i]) ^ ord(b[i])) + 1) for i in range(len(a)))
```

This code defines a function `string_xor` that performs the XOR operation on two input strings a and b using bitwise operations and returns the result as a string.

The type hints in the function signature tell the Python interpreter to expect strings as input. The function then performs a XOR operation on each character of the input strings and returns the result as a new string.