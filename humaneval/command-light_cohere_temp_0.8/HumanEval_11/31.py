```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Perform XOR operation on two strings consisting only of 0s and 1s.
    Return string consisting of 0s's and 1s
    """
    assert type(a) == str and type(b) == str
    assert len(a) == len(set(a)) and len(b) == len(set(b))
    assert all(a == '0' + '0'*len(a) and b == '0' + '0'*len(b))
    assert a == '0' + '1'*len(a) ^ b
    return a
```