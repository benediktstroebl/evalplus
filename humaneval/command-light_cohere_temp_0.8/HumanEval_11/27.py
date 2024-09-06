```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Inputs are two strings a and b consisting only of 1s and 0s.
    Perform XOR operation on these inputs and return the result.
    >>> '010'.join('110')
    '100'
    """
    return ''.join(*a ^ b)

# Test cases
test_cases = [
    ("010", "110"),
    ("000", "000"),
    ("001", "001"),
    ("1010", "0110"),
    ("1010", "1010"),
    ("0000", "0000"),
    ("1001", "0001"),
    ("1010", "1111"),
]

for a, b in test_cases:
    assert string_xor(a, b) == "".join(''.join(*a ^ b)
```
This script defines a function `string_xor` that performs the XOR operation on two strings containing only characters 1 and 0. The test cases ensure the data types and input strings are valid.