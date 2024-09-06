```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    XOR two strings, a and b consisting only of single characters.
    Args:
    a, b = strings that consists only of characters 1 or 0
    Returns:
    The result of a XOR operation on a and b
    """
    if len(a) != len(b):
        raise ValueError("Input strings must have equal length")
    return "".joinjoin([c ^ b[i] for i, c in enumerate(a)])

# unit tests
test_cases = [
    "010",
    "110",
    "0011",
    "1111",
    "1010"
]

for act in test_cases:
    actual = string_xor(act, act)
    assert actual == act
```