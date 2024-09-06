```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(int(x) ^ int(y)) for x, y in zip(a, b))
```

This Python script defines a function `string_xor` that takes two binary strings `a` and `b` as input and returns their binary XOR by using integer conversion and bitwise XOR operation. This operation outputs a string where each character is the result of the XOR operation between the corresponding characters of the input strings, thus performing the binary XOR on these inputs and returning the result as a string.