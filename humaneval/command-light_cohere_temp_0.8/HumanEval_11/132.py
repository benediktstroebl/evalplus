```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Inputs are two strings a and b consisting only of 1s and 0s.
    XOR = []
    for x in a:
        if x == '0':
            XOR.append(0)
        elif x == '1':
            XOR.append(1)
    return ''.join(XOR)
    """

This function performs a bitwise XOR operation on the two input strings, which are assumed to consist only of the character '1' and '0'. The function returns the result as a single string.