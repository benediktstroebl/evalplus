```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Function to perform XOR operation on two strings consisting only of ones.
    :param aa, b: Convert input strings to lists of characters and perform XOR operation.
    :return: Converted result back a string with only ones and 0s
    """
    a = [c for c in a if c == '1']
    b = [c for c in b if c == '1']
    return ''.join(c for c in a ^b)
```