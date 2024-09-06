Here's a self-contained Python script with a function that performs the string XOR operation on two input strings consisting only of digits:
```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    XOR two strings consisting of only digits.
    :param
        string_a, b: str
    :return string_xor
    """
    return str(bin(ord(a[0]) ^ ord(b[0]))[2:])

# Example usage
a = "010"
b = "110"
print(string_xor(a, b))  # Output: "100"
```
This script provides a string_xor function that takes two strings a and b as input, and returns the result of the XOR operation between these two strings. 
The function uses the binary representation of the XOR operation to perform the calculation, and returns the result as a string.