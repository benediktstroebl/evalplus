```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Inputs are two strings a and b consisting only of single characters.
    XOR is text and returns the result as a single string
    """
    return ''.join([c ^ b.charAt(ord(a[i]) for i, c in enumerate(b)])

# Test cases
test_cases = [
    '010', '110', '001', '0110', '100',
    '000', '110', '1'
]

for a, b in test_cases:
    got = string_xor(a, b)
    assert got == ''.join([c ^ b.charAt(ord(a[i]) for i, c in enumerate(b)])
```