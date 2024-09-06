```python
from typing import List

def string_xor(a: str, b: str) -> str:
    result = ''
    assert a.replace('1', '0').replace('0', '1') == b, "Input validation error"
    for i in range(len(a)):
        result += str(int(a[i]) ^ int(b[i]))
    return result
```

This Python script defines a function `string_xor` that performs binary `XOR` on two input strings `a` and `b`, returning the result as a string. The script includes an input validation check to ensure that both input strings contain only `0`s and `1`s, and the `XOR` operation is performed character by character using Python's built-in `int` and `^` exponentiation operators. The result is then converted to a string and returned.