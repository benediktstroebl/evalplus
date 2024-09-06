```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two strings consisting only of 1s and 0s.
    """
    XOR operation returns a string.
    Input strings must be provided as separate arguments, so we convert them to one list of strings
    """
    return "".join(c ^ int(a[0]) for c, a in zip(List(b), a))

# Test case
test_cases = [
    ("010", "110"),
    ("001", "010"),
    ("001", "001"),
    ("1010", "0110"),
    ("00", "1010")
]

for t in test_cases:
    actual = string_xor(*t)
    print(f"Expected: {t[0]} XOR {t[1]} = {actual}")
```