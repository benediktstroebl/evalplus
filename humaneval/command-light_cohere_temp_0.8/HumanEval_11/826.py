```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Inputs are two strings a and b consisting only of single characters.
    # XOR is the string a bitwise XOR of input strings
    """
    return f"{a ^ b}"  # Perform bitwise XOR and return result as a string

# Tests
test_string_xor = []
test_cases = [
    ("010", "110"),
    ("010", "001"),
    ("010", "11"),
    ("1010", "110"),
    ("1010", "001"),
    ("1010", "11"),
    ("110", "00"),
    ("001", "010"),
    ("110", "101")
]

for case in test_cases:
    actual = string_xor(*case)
    assert actual == case[1], f"Failed: {actual}, expected {case[1]}."
```