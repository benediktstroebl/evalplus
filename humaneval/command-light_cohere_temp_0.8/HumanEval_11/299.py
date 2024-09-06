```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    XOR two input strings containing only '0' and '1'
    Returns the XOR of a and b
    """
    return "".join(ord(c) == 1 for c in a ^& b)

# Test suite
test_cases = [
    ("010", "110"),
    ("001", "101"),
    ("100", "000"),
    ("1010", "1011"),
    ("000", "000"),
    ("110", "1110"),
    ("1111", "0000"),
]

for a, b in test_cases:
    actual = string_xor(a, b)
    assert actual == b, f"Error in test case: {a}, {b}, should be XOR {actual}"
```