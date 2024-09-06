```python
from typing import List

def string_xor(a: str, b: str) -> str:
    result = ''
    for i in range(len(a)):
        if a[i] != b[i]:
            result += '1'
        else:
            result += '0'
    return result
```

This script defines a function called `string_xor` that takes two strings `a` and `b` as input. It performs a binary XOR operation on these two strings and returns the result as a new string. The XOR logic checks if the corresponding bits of both strings are different (1 ^ 1 = 0, 0 ^ 0 = 0, 1 ^ 0 = 1, 0 ^ 1 = 1) and creates the result string accordingly.

The function is self-contained and does not rely on any external dependencies or additional code. It is a standalone function that can be executed independently to perform the binary XOR operation on two provided strings.