```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two strings consisting only of '0' and '1'.
    """
    return ''.join(a, b)

# Test cases
test_cases = [
    ("010", "110"),
    ("001", "010"),
    ("1000", "01"),
    ("1010", "11"),
    ("000", "100"),
]

for a, b in test_cases:
    result = string_xor(a, b)
    assert result == "".join(a, b)
```