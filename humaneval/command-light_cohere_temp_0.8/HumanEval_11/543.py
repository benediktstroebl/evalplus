```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Inputs are two strings a and b consisting only of single characters, return their XOR."""
    return a ^ b

# Test cases
test_cases = [
    ("010", "110"),
    ("abc", "cba"),
    ("abc", "123"),
    ("", "")
]

for a, b in test_cases:
    result = string_xor(a, b)
    assert result == "100"  # Example validation
```