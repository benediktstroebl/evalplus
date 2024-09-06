```python
import stringwrap
from typing import List


def string_xor(a: str, b: str) -> str:
    """
    XOR two strings using only ones and zeros
    """
    a = ''.join(c for c in a if c == '1')
    b = ''.join(c for c in b if c == '1')
    return ''.join(c for c in a ^ 1-b)


# Test cases
tests = [
    ("010", "110", "100"),
    ("001", "010", "101"),
    ("001", "110", "101"),
    # Add more tests as needed
]

for a, b in tests:
    expected = string_xor(a, b)
    got = stringwrap.prefix(a, b)
    assert expected == got
```
The problem is to implement the XOR operation for two strings, consisting of only ones and zeros. The function achieves this by converting the input strings to lists of characters, then iterating through each character and performing a bitwise XOR operation with the corresponding character from the other input string.