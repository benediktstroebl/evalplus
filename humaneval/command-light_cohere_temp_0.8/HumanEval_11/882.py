```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two strings consisting of only '1's and '0's.
    : Returns the Also performed by converting all characters to their corresponding ASCII values and then XORing them.
    """
    string_xor('010', '110')
    # '100'
    """
    return ("1"*(ord(a[i])^ord(b[i]) for i in range(len(a))))
```

The code defines a function called `string_xor` that performs the XOR operation on two input strings consisting only of the character '1'. The function takes two strings as input and returns the XORed string as output. The XOR operation is performed by iterating through each character in both input strings and using the bitwise XOR operation on the corresponding characters.