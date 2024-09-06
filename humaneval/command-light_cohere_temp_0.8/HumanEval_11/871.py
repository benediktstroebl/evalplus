```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting of only ones and zeros
    """
    # remove all zeros from both strings
    a = a.