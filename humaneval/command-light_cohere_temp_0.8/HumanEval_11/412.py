```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting only of characters 1 or 0
    """
    return ''.join(c ^ int('01'[b[i] == '1']) for i, c in enumerate(a + b))

# Test cases
test_cases = [
    ("010", "110"),
    ("1010", "01"),
    ("000110", "10"),
    ("101010", "0101010"),
    ("1111", "0000"),
]

for a, b in test_cases:
    result = string_xor(a, b)
    assert result == ''.join(int('01'[c] == 1) for c in result)
```