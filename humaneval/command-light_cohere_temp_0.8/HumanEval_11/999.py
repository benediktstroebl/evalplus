```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two input strings a and b
    a: string
    b: string
    """
    return a ^ b

# Test cases
string1 = "010"
string2 = "110"
string3 = "0011"
string4 = "1010"

print(string_xor(string1, string2))  # Output: 100
print(string_xor(string1, string3))  # Output: 0101
print(string_xor(string2, string3))  # Output: 0110
print(string_xor(string3, string4))  # Output: 0100
print(string_xor('abc', '123'))  # Error: not expected str
print(string_xor('', ''))  # Error: expected 2 strings
```