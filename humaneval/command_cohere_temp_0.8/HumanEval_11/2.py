```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(ord(x) ^ ord(y)) for x, y in zip(a, b))
```

This code solves the problem by performing the binary `XOR` operation on the two input strings `a` and `b`. Here is an explanation of the code:
1. The `typing` module is imported to ensure type correctness.
2. The function `string_xor` takes two strings a and b as input, emphasizing the requirement of performing binary `XOR` on these inputs, and returns the result of the operation as a string.
3. The function uses a `for` loop with a `zip` function to iterate over corresponding pairs of characters in `a` and `b`.
4. For each pair, the internal code of the characters (`ord()` function) of both elements is XORed (`^` operator), and the resulting binary code is converted back to a character using `chr()` and added to the accumulating result string.

This approach efficiently computes the binary `XOR` of two strings and returns the result as a string, fulfilling the problem statement's requirements.