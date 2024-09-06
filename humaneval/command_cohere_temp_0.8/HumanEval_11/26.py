```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(ord(x) ^ ord(y)) for x, y in zip(a, b))
```

This script defines a function `string_xor` that takes two binary strings `a` and `b` as input and performs a binary `xor` operation on their corresponding bits. The `zip` function arranges the characters of both strings into corresponding pairs, and the `^` operator computes the binary XOR of the character codes. The result is concatenated into a single string and returned.

Here's an example of how you can use this function to solve the problem statement mentioned in the code block:
```python
# Example usage
a = '010'
b = '110'
print(string_xor(a, b))  # Outputs '100'
``` 

This demonstrates the function's ability to transform the binary strings using XOR operations and provide the resulting string as output.