```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(int(x) ^ int(y)) for x, y in zip(a, b))
```

This script defines a function `string_xor` that takes two binary strings `a` and `b` as input and returns their binary XOR. The function uses `typing.List` to enable type-checking for the list of characters returned by the `zip` function. The `zip` function combines each corresponding character of `a` and `b` together to allow the `^` operator to perform the binary XOR operation on their ASCII values, which are converted to numbers. The resulting binary XOR is returned as a string with `'.join'` combined all resultant characters together. 

It is important to note that this code assumes that the input strings only contain digits '0' and '1'. If the input strings contain other characters, the code may not function as intended.