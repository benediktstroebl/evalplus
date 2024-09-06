```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(int(x) ^ int(y)) for x, y in zip(a, b))
```

This Python script defines a function `string_xor` that takes two binary strings `a` and `b` as input, where each character can be either a '0' or a '1'. It performs a binary XOR operation on the two strings and returns the result as a single string. 

The `zip` function is used to iterate over corresponding pairs of characters from both strings, and the `^` operator is used to perform the bitwise XOR operation on the pairs of integers. The result is then converted back to a string by using `chr` and appending the result to an empty string. This operation is done for all pairs, after which the resulting string is returned. 

This function efficiently computes the binary XOR of two strings in a straightforward manner.