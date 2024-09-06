```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform XOR operation on two strings consisting only of 0s and 1s.
    """ return ''.join([chr(x ^ y) for x, y in zip(a, b)])
 
    """
    assert len(a)==len(b), "Two strings must have the same length"
    assert all(c in '01' for c in a+b), "Input contains 0 or 1 but not both"
    return ''.join([chr(x ^ y) for x, y in zip(a, b)])
```