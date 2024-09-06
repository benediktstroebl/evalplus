```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(int(x) ^ int(y)) for x, y in zip(a, b))
```

This Python script defines a function `string_xor` that takes two binary strings `a` and `b` as input and returns their binary XOR by using `zip` to iterate over the corresponding pairs of digits and taking the binary XOR of the pairs. It is important to note that this function assumes that the input strings only contain digits '0' and '1'.