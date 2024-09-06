Here's the provided Python script:
```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    XOR two strings of only ones and zeros.
    :type aa = str
    :type b: str
    :rtype str
    """
    return ''.join(chr(ord(a[i]) ^ ord(b[i])) for i in range(len(a)))

# Test cases
strings = ['010', '110', '000', '111', '1001', '1010', '0202', '1212', '2030']
strings.

for s in strings:
    print(string_xor(s, s))
```
This script defines a function `string_xor` that performs a XOR operation on two strings, ensuring that only characters that are in one or the other are present in the result. It uses the type hints for more readable code. The provided test cases will then be passed to this function, and the result will be printed.