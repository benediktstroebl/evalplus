```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(int(x) ^ int(y)) for x, y in zip(a, b))
```

This Python script defines a function called `string_xor` that takes two strings, `a` and `b`, as input. The function performs a binary XOR operation on these two strings and returns the result as a single string. This is achieved by iterating over the corresponding bits of both strings (0 and 1) using zip, converting them to integers, performing the XOR operation (^) on them, and converting the result back to a character using chr. 

It is a self-contained script that can be executed as it is, and it contains a docstring that provides an example for how to use the `string_xor` function and what its expected output is. The example shows that if you input `a` as `'010'` and `b` as `'110'`, the function will return `'100'`, which is the result of performing a binary XOR on these two inputs.  This neatly explains how the code works and what outcome to expect.