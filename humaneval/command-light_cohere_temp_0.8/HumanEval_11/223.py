```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two strings consisting only of ones and zeros.
    """
    convert each string to list of characters
    perform XOR operation on each pair of characters and convert back to string
    """
    a = ''.join(char for char in a if char == '1')
    b = ''.join(char for char in b if char == '1')
    return ''.join(char for char in a if char == '0') + b
```