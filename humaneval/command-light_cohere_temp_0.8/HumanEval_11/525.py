```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform XOR operation on two strings consisting of only digits 1 and 0.
    Args:
    a, b ( both strings consisting only of digits 1 and 0)
    Return: str
    """
    return ''.join(chr((ord(a[i]) ^ ord(b[i])) if a[i] == b[i] else ord('0'))
# Tests
print(string_xor('010', '110'))
print(string_xor('000', '110'))
print(string_xor('01', '11'))
print(string_xor('1000', '01'))
print(string_xor('1010', '01'))
``` 
This function is a self-contained solution to the problem. It performs the string XOR operation by converting each input string into numbers and then performing the XOR operation on the corresponding numbers. 
The result is then converted back to a string using the `join` method, which concatenates characters in the result with those in the inputs.