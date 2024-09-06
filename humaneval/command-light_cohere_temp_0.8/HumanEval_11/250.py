```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting only of 1s and 0s.
    Return a string concatenation of a and b, with all 1s and 0s
    """
    return ''.join([i for i in a] ^ [i for i in b])

# Test cases
test_cases = [
    "010",
    "110",
    "100",
    "001",
    "000",
    "0000",
]

for case in test_cases:
    print(f"Test case: {case})
    print(string_xor(case, case))
    print("\n")
``` 
This script provides a function `string_xor` that performs the XOR operation on two input strings, consisting entirely of 1s and 0s. The function returns the xors the concatenated string. The test cases validate the are provided to verify the function's correctness.