```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    XOR two strings of only ones and zeros
    """
    return ''.join(c ^ d for c, d in zip(a, b))

# tests
test_cases = [
    "010", "110", "100",
    "101", "111",
    "000", "001"
]

for test_case in test_cases:
    actual = string_xor(test_case, test_case)
    assert actual == test_case
```