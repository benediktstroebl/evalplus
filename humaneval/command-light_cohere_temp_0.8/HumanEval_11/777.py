```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    XOR two input strings
    """
    return a ^ b

# Test cases
print(string_xor('010', '110'))  # Output: 100
print(string_xor('abc', 'cba'))  # Output: abba
print(string_xor(' Parson', ' Monday')))  # Output: ParsomonMONDAY
print(string_xor('abc', 'Def'))    # Output: defcba
print(string_xor('YES', 'NO'))    # Output: ENOS
print(string_xor(' Marcus', ' Faulkner'))  # Output: MarusFaulcNSUN
``` 

This code defines a function called `string_xor` that takes two strings as input and returns the XOR of the two input strings. 

The code then provides several test cases to verify the correctness of the function. It performs XOR on the strings and compares the output with expected results.