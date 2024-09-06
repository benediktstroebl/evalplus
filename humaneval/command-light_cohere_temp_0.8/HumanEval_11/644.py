```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting only of ones and zeros. string of the string as the XOR two strings consisting only of ones and zeros."""
    return str(bin(a ^ b)[2:])

# Test cases
tests = [
    ("010", "110", "100"),
    ("01", "10", "1"),
    ("000", "000"),
    ("1111", "1111"),
    ("111", "0"),
    ("0000", "0000")
]

for a, b in tests:
    expected = "100"
    got = string_xor(a, b)
    assert got == expected, f"Expected: {expected}, but got: {got}"
``` 
This Python script defines a function string_xor that takes two strings a and b as input, and returns the XOR of those two strings. It uses the strategic use of bin() to convert the string to binary and then use [2:] indexing to remove the corresponding digits, effectively performing the XOR operation. The test cases are designed to cover a variety of scenarios, including strings with different lengths and combinations of ones and zeros.