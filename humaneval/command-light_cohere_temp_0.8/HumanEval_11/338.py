```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two input strings a and b. XOR operation, return the result as a string
    """
    # Remove all occurrences of 0
    a = ''.join(c for c in a if c != 0)
    b = ''.join(c for c in b if c != 0)
    return f"{a ^ b}"

# Test cases
test_cases = [
    ("010", "110", "100"),
    ("1010", "0110"),
    ("10100", "01001"),
    ("000", "1111"),
    ("hello", "world"),
    ("aaaa", "aaaa"),
]

for a, b in test_cases:
    result = string_xor(a, b)
    assert result == "".join(result)
```