```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Perform XOR operation on two strings.
    assert len(a) == len(b),  
    assert len(set(a)) == len(set(b)),
    assert all(a == '0' if c == '0' else a == c for c in b),
    assert all(a == '0' if c == '1' else a == c for c in b),
    return a ^ b
```