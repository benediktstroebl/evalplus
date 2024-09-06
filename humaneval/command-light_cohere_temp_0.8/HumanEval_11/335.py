```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Inputs are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    """
   
    number of characters in the longer string is returned.
    """ return b if len(a) > len(b) else a"""

# Test cases
test_cases = [
    ("010", "110"),
    ("111", "010"),
    ("abc", "123"),
    ("abcdefghijklmnopqr", "abcdefghijklmnopu"),
    ("01234", "5678"),
    (" "", "" )
]

for a, b in test_cases:
    actual = string_xor(a, b)
    print(f"{a} XOR {b} = {actual}")
```