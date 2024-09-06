```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting only of digits 1 and 0.
    :param
    string_xor a: str, b: str
    :return str
    """
    return ''.join(c ^ int(b[0]) for c, b in zip(a, b))

# Test cases
test_cases = [
    "010",
    "110",
    "0011",
    "1111",
    "1010"
]

for test_case in test_cases:
    actual_xor = string_xor(test_case, test_case)
    print(f"Input: {test_case}, XOR: {actual_xor}")
```