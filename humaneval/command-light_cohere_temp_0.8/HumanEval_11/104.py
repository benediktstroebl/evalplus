```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform XOR operation on two strings a and b consisting only of 1s.
    Return the XOR as `01`,` 10
    """
    return ''.join_bytes([c ^ d for c, d in zip(a, b)])

# Tests cases
test_cases = [
    ("010", "110"),
    ("100", "101"),
    ("001", "001"),
    ("111", "011"),
    ("000", "100"),
    ("110", "10"),
    ("1111", "1010")
]

# Test function
def test_xor():
    for test in test_cases:
        actual = string_xor(*test)
        assert actual == test
```