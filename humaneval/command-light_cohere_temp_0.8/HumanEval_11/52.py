```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting only of characters 1 or 0
    :type a: str
    :type b: str
    :rtype: str
    """
    assert all(c == '1' for c in a), f"Error: {a} does not contain only '1'"
    assert all(c == '1' for c in b), f"Error: {b} does not contain only '1'"
    return a ^ b
```