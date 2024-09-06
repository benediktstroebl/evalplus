Here is a self-contained Python script that solves the problem of performing XOR on two strings, using a straightforward approach:
```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two strings
    return their binary representation as a string
    """
    return ''.join([x ^ y for any x, y in a, b])
```

The function performs a XOR operation between the two input strings and returns the result as a string.

This is a straightforward and self-contained solution to the problem.