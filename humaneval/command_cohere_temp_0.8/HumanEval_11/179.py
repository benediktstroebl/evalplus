```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(int(x) ^ int(y)) for x, y in zip(a, b))
```

This Python script defines a function called `string_xor` that takes two strings `a` and `b` as input. The function performs a binary XOR operation on these two strings and returns the result as a single string. This is done by using a list comprehension that takes pairs of corresponding elements from both strings, converts them to integers, performs the XOR operation, and converts the result back to a character using the `chr` function. 

The code also provides a docstring that includes a test case, demonstrating how to use this function to solve the binary XOR problem.