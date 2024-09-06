```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(int(x) ^ int(y)) for x, y in zip(a, b))
```

This Python script defines a function `string_xor` that takes two binary strings `a` and `b` as inputs, where each string only contains the characters '0' and '1'. The function performs a binary XOR operation on these two strings and returns the result as a single string. 

The `zip` function is used to iterate over corresponding pairs of characters from both strings, converting them into integers for the binary XOR operation, and then converting the result back to a character using `chr`.