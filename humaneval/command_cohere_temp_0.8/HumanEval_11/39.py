```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(int(a_char) ^ int(b_char)) for a_char, b_char in zip(a, b))
```

This script defines a function `string_xor` that takes two binary strings `a` and `b` as input and returns their binary XOR. The function uses a list of char_char pairings created by zip for char-level XOR and the `join` function to return the result as a string.

To test this, could you provide a test case that verifies the function's behavior? Test cases are valuable for ensuring the function's correctness and robustness. Let me know if you need any more help!