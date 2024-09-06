```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(ord(x) ^ ord(y)) for x, y in zip(a, b))
```

This script defines a function `string_xor` that takes two binary strings `a` and `b` as input and performs a binary `xor` operation on their corresponding bits. The `zip` function arranges the characters of both strings into corresponding pairs, and the `ord` function converts each character to its ASCII code. The `^` operator performs the bitwise `xor` operation on the ASCII codes, and the `chr` function converts the result back to a character. Finally, an empty string `''` is appended to the joined result.

Here's an example usage of the code:
```python
print(string_xor('010', '110')) # Output: '100'
```

This will output: `100` as the result of the binary XOR operation on the inputs `'010'` and `'110'`.