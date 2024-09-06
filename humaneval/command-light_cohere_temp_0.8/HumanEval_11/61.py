```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    XOR two strings of only digits using typescript
    """
    return ''.join(chr(ord(a[i]) ^ ord(b[i])) for i in range(len(a)))

# Test cases
test_string_xor = [
    '010', '110', '100',
    '0011', '1111',
    '001', '1110', '1010',
]

for t in test_string_xor:
    assert string_xor(t[0], t[1]) == t[2], f"Assert failed for {t}"
```
The function performs the XOR operation on two input strings and returns the result as a string. This function is with comprehensive tests that cover various test cases.