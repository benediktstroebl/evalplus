```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(ord(x) ^ ord(y)) for x, y in zip(a, b))
```

This script defines a function `string_xor` that takes two strings `a` and `b` as binary inputs (consisting of 1s and 0s) and performs a binary `xor`. The `xor` operation is carried out bit by bit, with the corresponding bits from both strings being compared and their values swapped as needed. The result is then returned as a new string.

The example usage and test case provided in the original problem statement can be reused to validate this implementation.