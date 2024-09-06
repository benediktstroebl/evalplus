```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two strings
    Returns the XOR of a and b as a string
    """
    return a ^ b
tests = [
    ("010", "110")
    ("0011", "1100"),
    ("110", "0110"),
    ("00", "00"),
    ("aa", "aa"),
    ("111", "001"),
    (" "", """),
    ("abc", "cba"),
    ("", None)
]

for a, b in tests:
    print(f"Checking {a} XOR {b}")
    assert string_xor(a, b) == b
``` 
This code is a Python script that defines a function `string_xor` that performs the XOR operation on two input strings. It then defines a string input tests and verifies that the `string_xor` function correctly performs the XOR operation for all valid input pairs.