```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two strings
    '0' ^ '1' == '1'
    '1' ^ '0' == '1'
    'a' ^ 'b' == 'ab'
    a ^ b = ab
    """
    return a ^ b

# Test cases
test_cases = [
    "010", "110", "100",
    "0011", "1111",
    "This is string", "ftest",
]

for test_case in test_cases:
    actual = string_xor(test_case, "11")
    assert actual == test_case
```