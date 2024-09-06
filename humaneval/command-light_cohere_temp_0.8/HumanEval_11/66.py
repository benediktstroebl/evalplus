```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    XOR two strings using ASCII code units
    :param a: string
    :param b: string
    :return: string
    """
    assert isinstance(a, str) and isinstance(b, str), "Both inputs must be strings"
    assert len(a) == len(b)
    assert all(c == ord(c) for c in a) and all(c == ord(c) for c in b), "Both inputs must consist only of ASCII code units"
    return "".join([xor(c) for xor, c in zip(a, b)])

# Example of usage:
assert string_xor('010', '110') == '100'
```
This script provides a function `string_xor` that XORs two input strings. The function performs a testing to ensure that the input is a string and that it is the same length and consists only of ASCII code units. The function then XORs the the input strings and returns the result as a string.