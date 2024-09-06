```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two strings containing only digits 1 and 0.
    """
    Input strings must only contain digits 1 and 0.
   
    Returns XOR on these digits and returns a string.
    """
    Test the XOR with:
    0010
    """
    assert len(set(a + b)) == 2, "Strings must contain only digits 1 and 0"
    return a ^ b
```