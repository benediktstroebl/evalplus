```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two strings composed of only 1s and 0s.
    :param[a] = string to perform XOR on
    :param[b] = string to perform XOR on
    :return = str
    """
    assert len(a) == len(b)
    assert all(c == '0' if c == '1' else c == '1' for c in a)
    assert all(c == '0' if c == '0' else c == '1' for c in b)
    return a ^ b
```
Do you need help with anything else?