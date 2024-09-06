```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(ord(x) ^ ord(y)) for x, y in zip(a, b))
```

This code solves the problem by performing the binary `XOR` operation on the two input strings `a` and `b`. Here is an explanation of the steps:
- The function `string_xor` takes two input arguments, `a` and `b`, which are compared character by character using the `zip` function.
- For each pair of characters, `x` from `a` and `y` from `b`, the `ord` function returns their ASCII values. 
- The bitwise `XOR` operation `^` is applied to these ASCII values, ensuring that 0x00 is XORed to produce 0x00, 0x01 is XORed to produce 0x01, and so on.
- The character corresponding to the resulting ASCII value is retrieved using the `chr` function.
- Lastly, the `join` function is used to concatenate all these XORed characters to produce the final result, which is returned. 

This approach efficiently performs binary `XOR` on two strings consisting of binary characters, providing the correct result as described in the problem statement.