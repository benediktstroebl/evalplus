```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Inputs are two strings a and b consisting only of digits '0' and '1'.
    Returns the XOR of the two input strings.
    >>> string_xor('010', '110')
    '100'
    """
    return chr(97 + (ord(a[0]) ^ ord(b[0])) % 256)

# tests
test_string_xor = [
    ("010", "110"),
    ("1010", "001"),
    ("000", "1111"),
    ("1011", "110"),
    ("0101", "1010"),
    ("1010", "1111"),
    ("1111", "0000")
]

for act, expect in test_string_xor:
    actual = string_xor(*act)
    print(f"Input: {act}, Expected: {expect}, Actual: {actual}")
```