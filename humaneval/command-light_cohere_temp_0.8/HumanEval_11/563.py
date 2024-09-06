```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting of only ones and zeros
    """
    return "".join([0] * len(a) ^ [1] * len(b))

# Test cases
test_cases = [
    ("010", "110"),
    ("0011", "1111"),
    ("000", "111"),
    ("1010", "0110"),
    ("1111", "0011"),
]

for test_case, expected in zip(test_cases, ["".join(expected) for expected in [string_xor(test,expected) for test in test_cases])):
    print(f"Test case: {test_case}, expected: {expected}, Result: {test_xor}")
``` 
Do you require assistance with anything else?