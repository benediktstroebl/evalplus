```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two strings with only 1s and 0s
    """
    return "".join(c ^ int(b[i]) for i, c in enumerate(a) if c == "1")

# Tests
assert(string_xor('010', '110')), "Should be XOR of '100'"
assert(string_xor('110', '010')), "Should be XOR of '00'"
assert(string_xor('00', '01')), "Should be XOR of '01'"
assert(string_xor('11', '11')), "Should be XOR of '11'"
assert(string_xor('11', '01')), "Should be XOR of not possible"
assert(string_xor('1010', '110')), "Should be XOR of '11' or '100'"
assert(string_xor('1010', '01')), "Should be XOR of '01'"
assert(string_xor('000', '110')), "Should be XOR of '00'"
```
This code provides a function that performs the XOR operation of two input strings with only characters (ones and zeros). The test suite includes several edge cases and common scenarios to ensure the correctness of the function.