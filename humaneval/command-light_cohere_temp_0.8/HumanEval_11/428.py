Here is a Python script that defines a function called `string_xor` solving the problem of XORing two strings consisting only of digits 1:s and 0:s:
```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting of only digits 1 and 0.
    Returns a string representation of the number result of the bitwise XOR operation on the two input strings.
    Parameters:
    a ( string ): 
       b ( string ) 
    Returns: 
       string
    """
    return ''.join(c ^ int(b[::-1]) for c, b in zip(a, b))
``` 

This script uses the `typing` module to add type hints to the function signature, which allows for better code readability and helps catch potential type-related bugs.