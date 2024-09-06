```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """Perform XOR operation on two strings"""
    return "".join(a ^ b)

# Test cases
test_cases = [
    ("010", "110"),
    ("abc", "cba"),
    ("", ""),
    ("text", "elve"),
]

for a, b in test_cases:
    result = string_xor(a, b)
    assert result == "100"
``` 
This Python script defines a self-contained function `string_xor` that performs the XOR operation on two input strings. The function utilizes the process to update the result, which is then tested using various test cases.