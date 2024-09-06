```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(int(x) ^ int(y)) for x, y in zip(a, b))
```

This Python script defines a function called `string_xor` that performs binary `XOR` on two strings `a` and `b`. The function takes in the two strings as input and returns the result of the binary `XOR` as a string. This is achieved by iterating over each character of the two strings, performing the `XOR` operation on the characters, and converting the result back to a character using the `chr` function. 

This operation is a basic technique in binary representation and can be useful in tasks such as encryption or data manipulation in binary formats. The function uses Python's typing module to define the types of the input parameters, ensuring type-safety in calling code, and returns the result as a string.