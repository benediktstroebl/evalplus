```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform XOR operation on two strings.
    a and return the string that concatenates the binary digits resulting from the XOR operation.

    """
    string_xor('010', '110')
    """
    # XOR operation
    # 010110 -> 010000
    # 10011010 -> 100000
    # 0010010 -> 00000
    result = ''.join((int(c) ^ int(b[::-1]) for c, b in zip('01' * a, '01' * b)))
    return result
```