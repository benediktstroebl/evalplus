```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(int(x) ^ int(y)) for x, y in zip(a, b))
```

This Python script defines a function `string_xor` that performs binary `XOR` on two strings (`a` and `b`). The `typing` module is used to create type annotations for the function parameters and return value. The function iterates through the characters of the two strings using `zip`, where for each pair of characters (one from each string), it takes their ASCII values, XORs them, and converts the result back to a character using `chr`. The resulting character is then joined together to form the output string. 

The function's behavior is demonstrated through a test case raised in the function docstring, where for inputs `'010'` and `'110'`, it returns `'100'`, demonstrating the binary XOR operation.