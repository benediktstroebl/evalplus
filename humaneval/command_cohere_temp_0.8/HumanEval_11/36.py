```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(ord(x) ^ ord(y)) for x, y in zip(a, b))
```

This code defines a function `string_xor` that takes two binary strings `a` and `b` as inputs, where each character can be either a '0' or a '1'. It performs a binary XOR operation on the two strings and returns the result as a single string. The process is carried out character by character, with the XOR operation being applied to the ASCII values of corresponding characters from `a` and `b`. The resulting character (0 or 1) is then appended to a growing string that constitutes the final result. 

The idea is to take the binary representation of the characters, perform XOR on the binary strings representing the two inputs, and convert the result back to a character. This approach leverages the intrinsic nature of binary XOR, which yields a 1 where the two bits are different and a 0 where the two bits are alike.

The given example in the problem statement entails `string_xor` being called with '010' and '110' as inputs. Applying XOR to these inputs yields '100', which is consequently returned by the function.