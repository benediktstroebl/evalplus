```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two strings, a and b, consisting only of digits 1 and 0.
    """:
    # type hints for better understanding of input arguments
    return "".join(chr((ord(a[i]) ^ ord(b[i]))  for i in range(len(a))))

# test case
print(string_xor('010', '110'))
``` 
This Python script defines a function called string_xor, which takes two strings as input and returns the XOR of these two strings. It uses a  `chr()` method and a for loop to convert each character of the input strings into integers and then XORs each corresponding character to get the result.