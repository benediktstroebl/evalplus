```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(int(x) ^ int(y)) for x, y in zip(a, b))
```

This Python script defines a function `string_xor` that takes two binary strings `a` and `b` as input, where each character can be either a '0' or a '1'. It performs a binary XOR operation on the two strings and returns the result as a single string. 

The `zip` function is used to iterate over corresponding characters in the two strings, where the `^` operator is used to calculate the binary XOR of the corresponding digits. Then, the result of the XOR operation is converted back to a string using the `chr` function and concatenated using the `join` function to produce the final XOR result as a string.