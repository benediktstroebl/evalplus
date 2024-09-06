```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Binary XOR operation on two strings, returns result as a string"""
    return ''.join(chr(ord(a[i]) ^ ord(b[i])) for i in range(len(a)))
test_cases = [
    "010".join(),
    "110".to_bytes(),
    "00".join_bytes(),
    "110" + "01"
]
for a, b in test_cases:
    assert string_xor(a, b) == "100"
```