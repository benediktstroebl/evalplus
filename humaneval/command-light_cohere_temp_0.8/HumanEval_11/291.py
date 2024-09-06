```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    XOR two strings consisting of only ones and zeros
    """
    # validate inputs
    assert len(a) == len(b), "Both inputs must have the same length"
    assert all(c == '0' or c == '1' for c in a), "All characters in the input must be either 0 or 1"
    assert all(c == '0' or c == '1' for c in b), "All characters in the input must be either 0 or 1"

    # XOR two strings
    result = ''.join(c ^ 2 for c in a) + ''.join(c ^ 2 for c in b)

    return result
```