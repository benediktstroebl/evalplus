```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    XOR two input strings a and b consisting only of ones and zeros.
    Return the XOR result as a string
    """
    return "".join(c ^ d for c, d in zip([str(a) for _ in range(len(a))), [str(b) for _ in range(len(b))]))

# Test the function
print(string_xor("010", "110"))
print(string_xor("0011", "1010"))
print(string_xor("000111", "000000"))
```