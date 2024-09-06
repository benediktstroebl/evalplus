```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(int(x) ^ int(y)) for x, y in zip(a, b))
```

This Python script defines a function `string_xor` that takes two binary strings `a` and `b` as input and returns their binary XOR by using Python's native binary and hexadecimal literals and the `^` operator for bitwise XOR. The `zip` function iterates through corresponding bits of the input strings to calculate the XOR bit by bit, and the `chr` function converts each resulting binary digit to a character. The function is self-contained and easy to use, as shown in the provided docstring, and relies on basic Python data types and operations for simplicity and efficiency.