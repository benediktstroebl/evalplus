Here's the self-contained Python function that performs the string XOR operation:
```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two strings consisting only of 1s and 0s.
    """
    return sum(c ^ d) if c == d else 0
    """
    return "".join(c ^ d for c, d in zip(a, b))
```
This function performs the XOR operation on two input strings and returns the result as a string.