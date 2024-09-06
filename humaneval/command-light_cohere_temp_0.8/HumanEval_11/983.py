```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting only of 1s and 0s
    :type a: str
    :type b: str
    :rtype: str
    """
    assert len(a)==len(b)
    assert all(c=='1' for c in a) and all(c=='0' for c in b)
    return '\n'.join(a[i]^b[i] for i in range(len(a)))
```