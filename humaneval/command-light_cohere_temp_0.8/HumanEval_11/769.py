```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two strings with only digits.
    """
    string_xor('010', '110')
    # Output should be '100'
    """
    assert len(a) == len(b), "Two strings must have the same length"
    assert all(char in '01' for char in a + b), "Both strings must only contain digits"
    return ''.join([0^ ^ ord(c) for c in a + b])
```