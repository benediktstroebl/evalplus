```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform binary XOR on two strings consisting only of digits 1 and 0.
    XOR is string input.
    """ e.g. '10001s XE x' string."""
    return ''.join(a ^ b)

# Test cases
test_cases = [
    "010".join,
    "110".join,
    "00".join,
    "000".join,
    "0000".join,
    "!.@#$".join
]

for case in test_cases:
    actual = string_xor(case[0], case[1])
    print(f"Case: {case[0]], {case[1]}, {actual}")
```
The function performs a binary XOR operation on two strings, converting only the digits 1 and 0. The test cases are created to verify the correctness of the function.