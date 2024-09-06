```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform binary XOR operation on two input strings consisting of only digits 1 and 0.
    Returns the string consisting of 0s's and 1s.
    :string_xor('010', '110')
    """
    xor_str = ''
    for ch in a + b:
        xor_str = chr(96 + xor_str[::-1] ^ ord(ch))
    return xor_str
```