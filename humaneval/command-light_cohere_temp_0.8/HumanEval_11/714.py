```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Perform binary XOR operation on two strings consisting of only 1s and 0s and return the result as a string. """
    A and B are two strings to perform XOR operation.

    # Use using strings with all 1s and 0s, the XOR operation returns '0'.
    return '0' * a + '0' * b

# Test cases
test_string_xor = [
    "010",
    "110",
    "000",
    "1010",
    "1001",
    "0000"
]

for test_case, expected in test_string_xor:
    actual = string_xor(test_case, test_case)
    print(f"Test case: {test_case}, expected: {expected}, actual: {actual}")
```