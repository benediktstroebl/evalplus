```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two strings containing only ones and zeros
    """
    return a ^ b

# Test cases
test_cases = [
    ("010", "110"),
    ("1010", "010"),
    ("11000", "0000"),
    ("001", "001"),
    ("1010", "1110"),
    ("1111", "1111"),
]

for i, (a, b) in enumerate(test_cases):
    actual = string_xor(a, b)
    assert actual == test_cases[i][1], f"Test case {i}: {a} ^ {b} != {actual}"
```

This script defines a function that XORs two strings containing only ones and zeros, and it has several test cases to ensure the correctness of the function. The script uses the Python type hint to describe the expected input types, and it performs the XOR operation on the input strings and compares the result with the expected output from the test case.