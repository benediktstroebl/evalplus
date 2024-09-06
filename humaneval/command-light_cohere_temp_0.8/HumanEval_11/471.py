```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two strings consisting only of 1s and 0s
    :param a: string
    :param b: string
    :return: string
    """
    # Check if inputs are strings
    if not isinstance(a, str) or not isinstance(b, str):
        raise TypeError("Both inputs must be strings")

    # XOR two strings
    return ''.join(x ^ y for x, y in zip(a, b))
```