```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform XOR operation on two strings containing only digits 1 and 0, and return the result as a string.
    Args:
        a: string, first string to perform XOR on.
        b: string, second string to perform XOR on.
    Returns:
    a XOR of a b
    """
    return "".join(a ^ b)

# Test cases
test_cases = [
    ("010", "110"),
    ("100", "01"),
    ("000", "000"),
    ("001", "101"),
    ("110", "11"),
    ("0000", "0000"),
]

for a, b in test_cases:
    result = string_xor(a,b)
    assert result == "".join(a ^ b)
```
This script defines a function **string_xor** that performs the XOR operation on two input strings containing only digits 1 and 0. It uses the string composing to perform the XOR and returns the result. It also includes a list of test cases that verify the function correctness.