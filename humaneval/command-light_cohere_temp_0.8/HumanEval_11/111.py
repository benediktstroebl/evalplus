```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two strings of only ones and zeros
    """
    return "".join(ord(c) ^ ord(b[i]) for i,c in enumerate(a + b))
# sample test
print(string_xor('010', '110'))
```