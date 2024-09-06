```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Inputs are two strings a and b consisting only of 1s and 0s,
    performs binary XOR operation on these inputs and returns the result as a string.
    >>> string_xor('010', '110')
    '100'
    """
    return a^b
```