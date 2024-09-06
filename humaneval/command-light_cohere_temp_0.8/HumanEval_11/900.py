```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting only of 1s and 0s.
    -> return theoo binary digits representing XOR of two inputs.
    """ In this code, we'll convert the inputs to lists of binary digits.
    return ''.join(list(a)) ^ .join(list(b))
"""
string_xor('010', '110')
```

This script defines a function called `string_xor` that performs the XOR operation on two input strings, which consist only of the characters '1' and '0'. The function returns the result as a string.

It uses the `typing` module to provide type hints for the function parameters and return value, and the operation is performed by using the bitwise XOR operation on the corresponding binary digits.