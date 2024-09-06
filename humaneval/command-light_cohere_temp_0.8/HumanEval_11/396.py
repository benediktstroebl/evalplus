```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    XOR two strings consisting only of 1s and 0s.
    Return: XOR and return a string
    """
    return a^b

# Test case
print(string_xor('010', '110'))
``` 
This script defines a function called `string_xor` that takes two strings a and b, consisting only of '1' and '0', and performs a bitwise XOR operation on those strings, returning the result as a new string.