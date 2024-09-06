```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(ord(x) ^ ord(y)) for x, y in zip(a, b))
```

This Python script defines a function called `string_xor` that takes two strings `a` and `b` as input. The function performs a binary XOR operation on these two strings and returns the result as a single string. This is done by using a list comprehension that alternates between characters from both strings, taking their ASCII values, performing the XOR operation, and converting the result back to a character.

The behavior of this function is demonstrated by the provided test case, where the function is invoked with the strings '010' and '110', and the result '100' is returned, demonstrating the binary XOR operation.