```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(int(a_char) ^ int(b_char)) for a_char, b_char in zip(a, b))
```

This Python script defines a function `string_xor` that performs binary `XOR` on two binary strings `a` and `b`. The `XOR` operation is performed bit by bit for each corresponding digit in the strings, and the result is returned as a string. This operation is fundamental in binary computation and can be useful in various applications involving data manipulation and cryptography.