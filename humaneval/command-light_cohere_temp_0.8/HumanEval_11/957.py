```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform XOR operation on two strings containing only ones and zeros.
    XOR = []
    for c in a+b:
        if c == '0':
            XOR.append(0)
        elif c == '1':
            XOR.append(1)
    return ''.join(XOR)
    """

This script defines a function `string_xor` that performs the XOR operation on two input strings a and b, which contain only ones and zeros. The XOR operation is performed by iterating over each character in the input strings and appending the corresponding XOR bits to a new list.

Finally, the function returns the string containing the XOR bits of the input strings.