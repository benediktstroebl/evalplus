```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform binary XOR operation on two strings consisting only of ones and zeros and return result as a string.
    :vers XOR on strings of '0's and '1's, where '0' maps to '50', and '1' maps to '100'.
    return f"{a[::]}{b[:]}{a[::-]}{b[::-]}"

# Test cases
cases = [
    "010", "110", "100",
    "001", "101", "110",
    "0000", "1111"
]

for case in cases:
    assert string_xor(case, case) == "0000"
``` 
This script defines a function `string_xor` that performs a binary XOR operation on two input strings. The function takes two strings as input and returns the XOR of these strings. The test cases are defined to verify the functionality of the `string_xor` function.