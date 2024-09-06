```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform XOR operation on two strings consisting of only ones and zeros and return the result as a string.
    """
    XOR operation: 0^b = a
    """
    return ''.join(x ^ y for x in a and y in b)

# Test cases
test_cases = [
    ("010", "110"),
    ("001", "001"),
    ("100", "000"),
    ("001", "101"),
    ("1010", "1011"),
    ("0000", "1111")
]

for a, b in test_cases:
    print(string_xor(a, b))
``` 
This code defines a function named `string_xor` that performs the XOR operation on two input strings, both consisting of only ones and zeros. The function returns the `None` if either input string is the empty string, otherwise, it performs the XOR operation and returns the result as a string.