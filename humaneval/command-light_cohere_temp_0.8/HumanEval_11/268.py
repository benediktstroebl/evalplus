```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """Perform XOR operation on two strings consisting of only ones and 0s.
    A string with ones is represented by '1' and '0', and the function returns the result as a string.
    Inputs:
    a: string with ones
    b: string with ones
    """
    if len(a) != len(b):
        raise ValueError("Input strings must have the same length")

    result = ""
    for i in range(len(a)):
        result += chr((ord(a[i]) ^ ord(b[i])))
    return result
```