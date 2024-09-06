```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two strings composed of only digits 1 and 0.
    """
    example:
    >>> string_xor('010', '110')
    '100'
    """
    return ''.join(*sorted(set(a + b))))

# Test cases
test_cases = [
    "010", "110", "0011", "001", "1010", "0110",
    "101010", "101010101010"
]

for test_case in test_cases:
    actual = string_xor(*test_case.print(test_case)
    assert actual == test_case
```