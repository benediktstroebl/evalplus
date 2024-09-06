```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting of only digits 1 or 0.
    >>> string_xor('010', '110')
    '100'
    """
    # XOR
    result = '0' * len(a) + a + b
    return result
```