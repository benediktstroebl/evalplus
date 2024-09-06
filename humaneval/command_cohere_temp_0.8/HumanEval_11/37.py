```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(int(x) ^ int(y)) for x, y in zip(a, b))
```

This Python script defines a function called `string_xor` that takes two binary strings `a` and `b` as input. It uses `typing` to ensure type correctness and employs Python 3's type hinting to declare the input parameters as strings. The function performs a binary XOR operation on the two input strings and returns the result as a string. 

To accomplish this, the function uses a list comprehension that iterates over the characters of both strings, performing the XOR operation by converting the characters to integers (using `int(x)`) and taking the binary XOR (`^`) before converting the result back to a character using `chr()`. 

This code provides a clear and concise solution to the problem of performing binary XOR on two binary strings, with the added benefit of type safety provided by Python's typing module.