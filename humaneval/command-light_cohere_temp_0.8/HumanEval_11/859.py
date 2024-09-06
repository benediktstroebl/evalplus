```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Inputs are two strings a and b consisting only of single characters.
    Returns binary XOR operation of the corresponding characters.
    Returns the XOR function on the inputs.
    >>> string_xor('010', '110')
    '100'
    """
    return ''.join_map(lambda x: (not (x == '0') ^ x != '1'), a + b)
```