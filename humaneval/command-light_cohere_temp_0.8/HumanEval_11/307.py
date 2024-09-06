```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two strings of only ones and zeros.
    Return result as a string
    """

    # assert the lengths of the input strings are equal
    assert len(a) == len(b)
    # XOR
    # a[i] ^ b[i]
    # = a[i] | b[i]
    # Using string concatenation and bitwise OR
    result = a + str(~b)
    return result
```