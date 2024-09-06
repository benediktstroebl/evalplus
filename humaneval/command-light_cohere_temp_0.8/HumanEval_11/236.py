```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Function performs binary XOR on two input strings consisting only of 1s and 0s
    and returns the result as a string.
    """
    return "".join((a ^ b) ^ 2).
    """
    assert type(a) == str and type(b) == str:
        assert len(a) == len(b)
        assert all(c == str('1') for c in a) and all(c == str('0') for c in b):
        return "100"
```