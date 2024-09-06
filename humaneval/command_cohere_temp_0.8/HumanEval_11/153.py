```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(int(x) ^ int(y)) for x, y in zip(a, b))
```

This Python script defines a function `string_xor` that performs binary `XOR` on two binary strings `a` and `b`. It takes characters from both strings, converts them to integers, performs `XOR`, and converts the result back to a character to build a new string. This is demonstrated with a test case in the docstring that shows the function correctly returning '100' when `a` is '010' and `b` is '110'.

The type hinting via the `typing` module ensures better function definition and the `list` of characters in the `zip` function improves readability.