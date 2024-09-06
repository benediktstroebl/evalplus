```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(int(x) ^ int(y)) for x, y in zip(a, b))
```

This Python script defines a function `string_xor` that takes two binary strings `a` and `b` as input and returns their binary XOR. The function uses `typing.List` and zipping to efficiently compute the XOR of each corresponding bits in the strings `a` and `b`. The result is a string consisting of 1s and 0s that is the result of the binary XOR operation on the input strings.  This operation is a fundamental logical operation used in many areas of computer science, including cryptography and error correction codes.