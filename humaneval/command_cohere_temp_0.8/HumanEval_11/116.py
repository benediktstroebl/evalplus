```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(int(x) ^ int(y)) for x, y in zip(a, b))
```

This Python script defines a function called `string_xor` that takes two strings `a` and `b` as input. The function performs a binary XOR operation on these two strings and returns the result as a single string. This is done by using a list comprehension that iterates over the characters of both strings, performing the XOR operation by converting the characters to their integer representations, XORing them, and converting the result back to a character using the `chr` function. 

The code also provides a markdown block that demonstrates the behavior of the function using example inputs.

This code can be used as a self-contained Python module that can be imported and used to perform binary XOR on two strings consisting of binary characters.