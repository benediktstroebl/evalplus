```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform binary XOR operation on two strings and return result as a string.
    :param a a: str, the first string containing only ones and 0s
    :param b: str, the second string containing only ones and 0s
    :return: str, the result of the XOR operation
    """
    return ''.join(a^b)
```