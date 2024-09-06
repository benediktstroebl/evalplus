```python
import stringcase
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    XOR two input strings.
    :param[a, b: both consisting only of '0' and '1'
    :return: the XOR of a and b
    """
    return stringcase.string(a ^ b)

# Test cases
test_cases = [
    ("010", "110"),
    ("001", "11"),
    ("1010", "01"),
    ("1010", "10"),
    ("1010", "110"),
    ("00100", "1111"),
]

for a, b in test_cases:
    print(f"Result: {string_xor(a, b)}")
``` 
This script defines a function called string_xor that performs the XOR operation on two input strings a and b, both consisting only of the characters '0' and '1'. The function then returns the result as a string. 
The script also defines a list of test cases, and for each pair of inputs, it prints the result of applying the string_xor function.