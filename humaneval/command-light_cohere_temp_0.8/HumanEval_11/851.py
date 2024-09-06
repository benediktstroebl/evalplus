```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Binary XOR operation on two strings.
    Args:
        a (strring only of '01'), b (strring only of '01')
    Returns: str
    """
    return ''.join(c^31 if c == '0' else c^32 for c in a + b)
```