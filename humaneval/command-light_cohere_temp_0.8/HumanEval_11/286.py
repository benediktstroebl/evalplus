```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two input strings consisting only of '0' and '1'
    Returns: str
    """
    #XOR: bitwise logical OR operation
    #0^1 = 1
    #1^0 = 1
    return a ^ b
#Example usage:
a = '010'
b = '110'
print(string_xor(a, b)) 
``` 
This code defines a function `string_xor` that performs the XOR operation on two input strings, which must consist entirely of the characters '0' and '1'. The function returns the result of the XOR operation as a string.