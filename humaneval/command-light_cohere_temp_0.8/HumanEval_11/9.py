Here is a self-contained Python script that solves the problem of performing the XOR operation on two input strings, and returns the result as a string:
```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two strings consisting only of digits 1 and 0.
    Example: https inputs
    """
    return ''.join(a^b)
```

This script defines a function named `string_xor`, which takes two input strings `a` and `b` as arguments. The function performs a XOR operation on these strings, and returns the result as a single string.