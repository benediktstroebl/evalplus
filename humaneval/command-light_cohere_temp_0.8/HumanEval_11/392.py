```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Function to perform XOR operation on two strings consisting only of '1's and '0's.
    """
    'result' = a ^ b
    return result

# Test cases
test_cases = [
    ("010", "110"),
    ("001", "101"),
    ("1010", "01"),
    ("0011", "11"),
    ("110", "001"),
    ("1111", "1111")
]

for idx, (a, b) in enumerate(test_cases):
    result = string_xor(a, b)
    assert result == test_cases[idx + 1], f"Failed at test case {idx + 1}"
```  The function performs a basic XOR operation on two strings and returns the result as a string.