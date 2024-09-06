```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two strings using only ones and zeros.
    """ Convert the common string representation of numbers to strings.
    Return the mathematical XOR operation
    then perform bitwise XOR operation and return result.
    """ The general operation is 1010^8 - 1.
    """
   
    generate binary representation of numbers using
    list(bin(i)[2:] for binary representation of i up to the number.
    """ convert it list of binary digits into a string using list comprehension
    """
    # convert the number to a string
    a = ''.join(bin(int(a, 2))[2:])

    # convert the number to a string
    b = ''.join(bin(int(b, 2))[2:])

    # XOR the strings
    result = ''.join(a ^ b)

    return result
```