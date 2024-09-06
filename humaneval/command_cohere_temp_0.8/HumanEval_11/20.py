```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return bin(int(a, 2) ^ int(b, 2))[2:]
```

This Python script solves the problem by taking two input strings `a` and `b` consisting only of 1s and 0s. It performs binary `XOR` on these inputs, converts the result back to a string format, and returns it. This is achieved by using the binary representation of the numbers, performing the XOR operation, and converting it back to a string format.

For example, if you call the function like `string_xor('010', '110')`, it will return `'100'` as the result of the binary XOR operation.

This approach leverages the binary representation of numbers to perform the XOR operation efficiently, ensuring accurate results for binary strings. It provides a clear and concise solution without external dependencies.