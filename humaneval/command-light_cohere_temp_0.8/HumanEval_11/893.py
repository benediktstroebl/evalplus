Here is a self-contained Python script that solves the problem of performing a string XOR operation:
```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    XOR two input strings consisting only of ones and zeros.
    Returns the string containing only ones and zeros.
    """
    string_xor('010', '110')
    """

    # Convert the input strings to lists of characters
    alist = List(filter(str.isdigit, a))
    blist = List(filter(str.isdigit, b))

    # Use the built-in function list.get() to return the string of ones and zeros
    result = ''.join([lst.get(ord(c), blist.get(ord(c))) for c in '0123456789'])

    return result
```

This script defines a function called `string_xor` that performs the XOR operation on two input strings. It uses the filter to convert the input strings into lists of characters, and then uses the `get()` method to convert the characters into strings of ones and zeros. The result is then obtained by XOR operation of the two strings.