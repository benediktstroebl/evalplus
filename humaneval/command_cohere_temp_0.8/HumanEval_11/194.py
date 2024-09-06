```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(int(x) ^ int(y)) for x, y in zip(a, b))
```

This Python script defines a function called `string_xor` that takes two strings, `a` and `b`, as input. The function performs a binary XOR operation on these two strings and returns the result as a single string. This is done by using a list comprehension that takes pairs of corresponding elements from both strings, converts them to integers for the binary XOR operation, and then converts the result back to a character using `chr`. 

The `typing` import establishes the use of type annotations, which improve code readability and maintainability, providing hints to the programming language about the expected types of inputs and outputs. 

This solution is self-contained and can be easily copied and ran independently to test and verify its functionality.