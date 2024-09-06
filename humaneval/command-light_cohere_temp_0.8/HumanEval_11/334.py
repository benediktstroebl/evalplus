```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    XOR two strings using bitwise operation.
    Convert input strings to lists of integers, then perform bitwise XOR operation on each integer in parallel.
    Returns the string of the resulting bits.
    Args:
        string a: first input string
        string b: second input string
    Returns:
        string: result of XORing two input strings
    """
    a = [ord(char) for char in a]
    b = [ord(char) for char in b]
    return ''.join(''.join([chr(i ^ 32 - (1 << (j - i))) for i, j in zip(a, b)])
```
Do you need assistance with any other Python-related tasks?