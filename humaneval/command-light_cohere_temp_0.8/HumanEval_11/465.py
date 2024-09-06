```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Inputs are two strings a and b consisting only of single characters.
    perform XOR on the string inputs, and return the result as a string.
    >>> string_xor('010', '110')
    '100'
    """
    return ''.join([c ^ d for c in a for d in b])
```