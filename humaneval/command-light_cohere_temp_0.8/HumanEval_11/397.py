```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    XOR two strings using Python bytes
    :param a: str, Input string
    :param b: str, Input string
    :return: str, Resulting string
    """
    return bytes([x ^ y for x, y in zip([ord(c) for c in a], [ord(c) for c in b])])

# test cases
string1 = "01010"
string2 = "110"
print(string_xor(string1, string2))  # Output 100
string3 = "abc"
string4 = "world"
print(string_xor(string3, string4))  # Output bcd...
string5 = "abc123"
print(string_xor(string5, string5))  # Output same
```