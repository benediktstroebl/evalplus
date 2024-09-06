```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting of only ones and zeros
    """
    # similar to xor in C++
    return a ^ b

# Test case
test_cases = [
    "010", "110", "00110", "001", "0110",
    "100"
]

for test_case in test_cases:
    actual = string_xor(test_case, "0")
    print(f"Expected: {test_case} , Actual: {actual}")
```