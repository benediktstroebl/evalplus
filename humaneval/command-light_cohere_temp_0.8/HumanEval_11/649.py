```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform XOR operation on two strings and return result as a string.
    """
    strings must only consist of 1s and 0s.
    return ''.join([x((ord(a[i]^b[i]) for i in range(len(a)))])
    """
    return "".join([chr((ord(a[i])^ord(b[i])) for i in range(len(a)))])
```