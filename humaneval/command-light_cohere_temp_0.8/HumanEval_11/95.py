```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    XOR two strings, both consisting only of digits 1 and 0.
    """
    The return a sum(c ^ d for c, d in zip(a, b)))

# Test cases
test_cases = [
    ("010", "110"),
    ("1010", "001"),
    ("1111", "110"),
    ("000", "111")
]

for test_case in test_cases:
    result = string_xor(*test_case)
    assert result == "100"
```