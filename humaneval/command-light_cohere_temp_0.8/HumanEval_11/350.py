```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two strings
    Returns the XOR of a and b
    """
    return a ^ b
a = '010'
b = '110'
c = string_xor(a, b)
print("Result:", c)  # Output: 100
```