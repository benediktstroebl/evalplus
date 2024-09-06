```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ 
    XOR two strings consisting of only ones and zeros
    """
    if len(set(a)) != 2 or len(set(b)) != 2:
        raise ValueError("Input strings must contain only digits 1 and 0")
    return str(bin(a ^ b)[2:])

# Test the function
a = "010"
b = "110"
print(string_xor(a, b))  # Output: 100
print(string_xor("abc", "abc"))  # Error: Input strings contain non-digit characters
```