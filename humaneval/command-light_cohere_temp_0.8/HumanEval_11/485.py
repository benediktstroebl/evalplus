```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two strings consisting only of '0' and '1'
    Returns: result, the XOR of a and b
    """
    return "".join(ord(x) ^ ord(y) for x, y in zip([a, b]))
# Unit tests
tests = [
    ("010", "110", "100"),
    ("001", "010", "001"),
    ("1010", "1001"),
    ("1111", "0000"),
]
for a, b in tests:
    assert string_xor(a, b) == b, f"Failed for {a} and {b}"
``` 
This code defines a function that performs the XOR operation on two input strings, consisting only of 0s and 1s. It uses the by using the zip function to iterate over pairs of characters from both input strings and performs the XOR operation using the `ord` property of each character. The resulting string is then only the XOR of the corresponding characters.