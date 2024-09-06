```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return '{0}{1}{2}'.format(a[0] ^ b[0], a[1:] ^ b[1:], a[-1] ^ b[-1])
```

The provided Python script defines a function called `string_xor` that takes two strings `a` and `b` as input. This function performs a binary `XOR` operation on the input strings `a` and `b`, which consist of only 1s and 0s. It then returns the result of the `XOR` operation as a string.

The script employs Python's typing module to enable type hints, enhancing code clarity and usability. The `string_xor` function uses formatted string literals (`{0}{1}{2}`) to efficiently combine the results of the binary `XOR` operations on the first character, remaining characters, and last character of the two input strings.