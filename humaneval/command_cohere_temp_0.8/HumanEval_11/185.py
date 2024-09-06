```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(int(x) ^ int(y)) for x, y in zip(a, b))
```

This Python script defines a function called `string_xor` that performs binary XOR on two input strings consisting of only 1s and 0s. The function takes two strings `a` and `b` as arguments and returns their binary XOR as a string. It uses `typing` for type hints and the `zip` function to ensure that the characters are XORed pairwise. The join operation concatenates the binary strings into a single string. 

This code can be used as a standalone script to perform binary XOR on two input strings and produce a result string.  It can be used with inputs such as `['010', '110']` to produce a result of `100`.  Such XOR operation may be useful in binary masking and other bit-wise operations.