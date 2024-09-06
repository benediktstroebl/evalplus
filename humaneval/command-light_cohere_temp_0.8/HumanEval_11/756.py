Here's a self-contained Python function that performs the string XOR operation:
```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform XOR on two input strings a and b
    >>> string_xor('010', '110')
    '#100'
    """
    return '#' + a ^ b
```
This function takes two input strings a and b consisting only of digits '0' or '1' and performs the XOR operation on them, producing a new string with only the hash value.