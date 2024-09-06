Here is a self-contained Python function that solves the problem of XORing two strings:
```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two strings containing only ones
    Returns the result of XORing a and b
    """
    return ''.join(c if c != '0' else 0 for c in a) ^ b
```
Do you require assistance with any other Python tasks?