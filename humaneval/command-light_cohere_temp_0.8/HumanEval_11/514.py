```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Inputs are two strings consisting of only '1' and '0', performs XOR binary operation and returns the result as a string."""
    return ''.join(a ^ b)

# Test cases
print(string_xor('010', '110'))  # Output: 100
print(string_xor('000', '111')))  # Output: 101
print(string_xor('1111', '1111')))  # Output: 000000
print(string_xor('0000', '1111')))  # Should raise an error
```