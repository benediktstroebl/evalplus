```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    XOR two strings containing only '0's and '1's
    Returns the XOR'd string
    """
    return ''.join(*(i ^ j for i, j in zip(a, b)))

# Test cases
test_cases = [
    "010",
    "110",
    "0011",
    "1010",
    "1001"
]

# Loop through test cases
for tc in test_cases:
    print(tc, end=' -> ')
    result = string_xor(tc[0], tc[1])
    print(result, end='\n')
``` 
This script defines a function `string_xor` that takes two strings as input and returns the XOR of the two strings. It uses the string contents of only '0's and '1's as inputs and performs the XOR operation, which returns the result as a string.

The script also includes a list of test cases, and loops through the test cases, printing each input pair and the corresponding result. The test cases ensure that the function is working correctly for various inputs.