```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform binary XOR on the inputs and return result.
    >>> string_xor('010', '110')
    '100'
    """
    return "".join(chr(ord(a[i]) ^ ord(b[i])) for i in range(len(a)))
```