```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(int(x) ^ int(y)) for x, y in zip(a, b))
```

This Python script defines a function called `string_xor` that performs binary `XOR` on two input strings `a` and `b`, which consist only of `1`s and `0`s. The function takes two strings as arguments and returns their binary `XOR` as a string. It uses `typing` to ensure type-safety and employs `zip` and `chr` to perform the `XOR` operation on the character integers. 

This solution survives inside a code block as it is standalone and does not rely on external variables or functions. It can be executed directly in a Python environment that supports type-hinting and the necessary syntax. 

To ensure compatibility, please note that this script is compatible with Python 3 due to its use of typing and syntax. Also, ensure that the strings you input for `a` and `b` are confined to contain only 0s and 1s to evade any misinterpretation or error during the binary `xor` calculation.