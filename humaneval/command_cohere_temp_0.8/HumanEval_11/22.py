```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(int(x) ^ int(y)) for x, y in zip(a, b))
```

This Python script defines a function called `string_xor` that takes two strings, `a` and `b`, as input. The function performs a binary XOR operation on these two strings and returns the result as a single string. This is done by using a list comprehension that zips the two strings and takes the XOR of the corresponding characters' ASCII values using the `^` operator, which has the integer XOR operation as its default Python 3 bitwise operator, and then converts it back to a character using `chr`.

The function is designed to be self-contained, meaning that it does not rely on any external variables or contexts. It uses the `typing` module to improve code readability with type annotations and can be called from other parts of the code with different string inputs to perform the binary XOR operation, fulfilling the problem statement and test case requirements.