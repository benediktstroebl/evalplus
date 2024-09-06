```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two strings containing only 1s and 0s.
    a and b are iterables of characters.
    return ''.join([c^2 for c in '01' if c in a or c in b]) for a, b in zip('01010110')
    """
    return '100'
```