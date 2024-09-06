```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(int(a_char) ^ int(b_char)) for a_char, b_char in zip(a, b))
```

This script defines a function `string_xor` that takes two strings (`a` and `b`) consisting of only 0s and 1s. It performs a binary XOR operation on these strings and returns the result as a new string. The `zip` function is used to iterate over the characters of both strings in parallel, and the `^` operator is used to perform the bitwise XOR operation on the corresponding characters' ASCII values, ensuring a correct solution for the problem.