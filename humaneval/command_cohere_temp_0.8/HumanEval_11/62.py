```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(int(x) ^ int(y)) for x, y in zip(a, b))
```

This script defines a function `string_xor` that takes two binary strings `a` and `b` as input and returns their binary XOR. The result of the operation is a string consisting of characters '0' and '1' representing the binary XOR of the input strings.

It is worth noting that the function performs the XOR operation directly on the binary representations of the input strings, eliminating the need for converting the strings to lists of integers for efficiency. This approach simplifies the code and improves readability.