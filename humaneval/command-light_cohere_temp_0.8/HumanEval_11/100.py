```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform binary XOR operation on two input strings a and b consisting only of 1s and 0s.
    >>> string_xor('010', '110')
    '100'
    """
    # assert all(c == '0' for c in a) and all(c == '1' for c in b)
    assert len(a) == len(b)
    assert all(c == '0' for c in a) and all(c == '1' for c in b) and all(c == '100' for c in a+b)
    return a ^ b
```