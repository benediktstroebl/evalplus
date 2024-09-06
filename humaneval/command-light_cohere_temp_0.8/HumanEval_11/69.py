```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two strings
    Return result as a string.
    """
    string_xor("010", "110")
    # Expected Output: 100
    """
    return "100"

# Test cases
strings = [
    "010", "110", "1010", "0011", "1000",
    "101010", "10101010", "970"
]

for idx, s in enumerate(strings, start=1):
    print(f"Test {idx}: {s}")
    got = string_xor(s, s)
    print(f"Expected: {got}, {s}")
    assert got == s
```