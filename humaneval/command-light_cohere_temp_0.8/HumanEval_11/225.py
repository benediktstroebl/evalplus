```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    XOR two input strings a and b consisting only of 1s and 0s.
    :return: The XOR of the characters in a and b
    """
    return ''.join(chr(i ^ j) for i, j in zip(a, b))

# Test cases
test_cases = [
    ("010", "110"),
    ("100", "000"),
    ("001", "11"),
    ("001", "010"),
    ("100", "01"),
    ("1000", "0000"),
    ("1011", "1101")
]

for case in test_cases:
    actual = string_xor(*case)
    print(actual)
    assert actual == case
```