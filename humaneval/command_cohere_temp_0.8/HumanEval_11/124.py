```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(ord(x) ^ ord(y)) for x, y in zip(a, b))
```

This script defines a function `string_xor` that takes two strings `a` and `b` as binary inputs (consisting of 1s and 0s) and performs a binary `XOR` operation on them. The `XOR` operation returns a string with characters corresponding to the bits of the two input strings.

The function ultimately returns the `XOR`'ed string. This is achieved by using a list comprehension that iterates over the characters of both strings, performing the `XOR` operation on their ASCII values and joining the resulting characters into a string.

This solution adheres to the problem statement and provides an efficient way to compute the `XOR` between two binary strings.