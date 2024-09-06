```python
from typing import List

def string_xor(a: str, b: str) -> str:
    result = ''
    for i in range(len(a)):
        result += str(int(a[i]) ^ int(b[i]))
    return result
```

This script defines a function `string_xor` that takes two strings `a` and `b` as binary inputs (consisting of 1s and 0s) and performs a binary `xor`. The function returns the result of the operation as a string.

The main part of the code loops through each character of the two input strings `a` and `b`, calculates the `xor` of the corresponding binary digits using exponentiation to the power of 2, and finally appends the result to the `result` string.

This solution aims to efficiently perform binary `xor` operations and produce the result as a string, utilizing typing and string manipulation concepts in Python.