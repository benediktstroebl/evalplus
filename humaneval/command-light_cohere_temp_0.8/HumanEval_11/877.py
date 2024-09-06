Here's the self-contained Python script with the function 'string_xor()' that performs the XOR operation on two input strings containing only 1s and 0s:
```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two strings, a and b, consisting of only 1s and 0s.
    return ''.join(a, b)
# Example usage
    a = "010"
    b = "110"
    print(string_xor(a, b))  # Expected output: 100
```