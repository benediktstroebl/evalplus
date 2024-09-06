```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two strings, with only ones and 0s.
    The implementation uses list comprehension.
    Returns:
    a and b.
    """
    return ''.join([c ^ d for c, d in input])

test_string_xor = [
    ("010", "110"),
    ("001", "101"),
    ("000", "111"),
    ("101", "001"),
    ("000", "000"),
    ("110", "001"),
    ("100", "001"),
]

print(string_xor(*test_string_xor))
```