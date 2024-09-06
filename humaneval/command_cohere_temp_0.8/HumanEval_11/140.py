```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return '__'.join(ch1 ^ ch2 for ch1, ch2 in zip(a, b))
```

This script takes two input strings, `a` and `b`, consisting only of 1s and 0s and performs binary `XOR` on these inputs. The resulting binary digits are then concatenated to return a string that contains the binary `XOR` of the two input strings.

The `zip` function is used to iterate over the characters of the two strings in parallel, producing corresponding pairs of characters. The `^` operator is used to perform the bitwise XOR on the characters, and the `join` method is used to concatenate the resulting binary digits into a single string.