```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two strings using list comprehension and bitwise XOR operator.
    return ''.join(map(lambda x: x^64, a)) + b
    """
    return ''.join(map(lambda x: x^64, a)) + b
```