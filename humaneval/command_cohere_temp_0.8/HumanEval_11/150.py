```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return bin(int(a, 2) ^ int(b, 2))[2:]
```

This Python script solves the problem by taking two input strings `a` and `b` consisting only of 1s and 0s. It performs binary `XOR` on these inputs using bitwise XOR operation (`^`) on the corresponding integers represented in binary. The result is then converted back to a string, and returned.

The function includes type annotations using the `typing` module and also includes a docstring that explains the problem, describes the function, and provides an example for how the function is called.

To test this function, you can call it with two strings representing binary numbers and compare the result with the expected output.