```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Returns the XOR of two strings a and b consisting only of single characters.
    :string_xor('010', '110')
    # True
    '100'
    """
    # XOR all single characters
    result = '0' + '1'*len(set(a) ^ set(b)))
    return result
```