```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    XOR two strings consisting only of ones and zeros
    Returns: 0101 if a==b else a^b
    """
    if a == b:
        return '0101'
    return a^b

# Test cases
test_cases = [
    "010", "110", "100", "001", "000"
]

for test_case in test_cases:
    actual = string_xor(test_case, test_case)
    print(f"Case: {test_case}, Result: {actual})
```