```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Takes two strings a and b consisting only of single characters, returns their XOR.
    >>> string_xor('010', '110')
    '100'
    """
    # Perform XOR on the two input strings
    result = ''.joinjoin([c ^ d for c in a and d in b])
    return result
```