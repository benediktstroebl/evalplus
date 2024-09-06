```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform XOR operation on two strings containing only ones.
    a XOR operation: a ^ b = a & b
    """
    return a ^ b

# Test cases
test_cases = [
    ("010", "110"),
    ("0011", "11"),
    ("001", "1010"),
    ("00", "10"),
    ("1111", "01")
]

for a, b in test_cases:
    print(f"Input: {a}, {b}")
    print(f"Expected Output: {string_xor(a, b)}")
``` 
This script defines a function `string_xor` that performs the XOR operation on two input strings and returns the result as a string. The function is tested with five test cases and the output is displayed for each case.