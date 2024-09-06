```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two strings using binary representation.
    Returns a string representation of a binary number 1010 and
    append it to string b.
    Do this operation for all string until the length of both strings is equal.
    Return the result string containing all XOR'd characters.
    """
    example:
    If a = '010' and b = '110', 
    return '100'
    """
    result = []
    while len(a) != len(b):
        result.append(a[0])
        a = a[1:]
    result.append(b[0])
        b = b[1:]
    return ''.join(result)
```