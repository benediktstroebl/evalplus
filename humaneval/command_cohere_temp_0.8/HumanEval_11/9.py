```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(int(x) ^ int(y)) for x, y in zip(a, b))
```

This Python script defines a function called `string_xor` that takes two binary strings `a` and `b` as input. It uses `typing` to ensure type safety and employs `zip` to iterate over the characters of `a` and `b` in parallel. For each pair of corresponding characters, it applies the binary XOR operation (`^`) on the corresponding integers, converts the result back to a character using `chr`, and combines these characters to form the output string. 

The function's docstring includes a test example that demonstrates how it can be invoked with specific inputs and verifies the correct behavior against the given challenge. 

This approach efficiently solves the problem by directly performing binary XOR on the character integers and producing a character string as the final result.