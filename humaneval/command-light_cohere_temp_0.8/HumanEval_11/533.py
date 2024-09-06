```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform binary XOR on two strings.
    assert len(a) == len(b),
    assert all(c == ord(a[i]) ^ ord(b[i]) for i, c in enumerate(a)),
    assert all(c == ord(a[i]) ^ ord(b[i]) for i, c in enumerate(b)),
    return ''.join('0' * (len(a) - 1) + a + b)
```