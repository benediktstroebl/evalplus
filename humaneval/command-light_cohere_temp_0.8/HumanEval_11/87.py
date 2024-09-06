```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting of only ones and zeros.
    a = ''.join(a) ^ b
    return a
    """

    assert len(a) == len(b) == 10, "Input strings must be 10 characters long"
    assert all(c == '0' or c == '1' for c in a + b), "Both inputs must only contain ones and zeros"
    assert sorted(a) == sorted('10101010'), "Input strings must be in alphabetical order"
    return a
```