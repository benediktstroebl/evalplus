```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(int(x) ^ int(y)) for x, y in zip(a, b))
```

This script defines a function `string_xor` that takes two binary strings `a` and `b` as input and returns their binary XOR by using bitwise XOR operation on the corresponding characters/bits in the strings. The `zip` function is used to pair the characters of both strings for the XOR operation, and `chr` is used to convert the resulting binary numbers back to characters.