Here is a Python script with a self-contained function that solves the problem of performing a string XOR operation:
```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two strings
    Inputs are two strings a and b consisting only of 1s and 0s
    Returns the XOR of a and b
    """
    return ''.join(chr(a^b[i]) for i in range(len(a)))

# Test cases
tests = [("010", "110") , ("001", "001"), ("1010", "01")]
print(string_xor(*tests)) # Output should be 100
```