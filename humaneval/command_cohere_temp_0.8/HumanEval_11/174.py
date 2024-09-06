```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return '__'.join(c^b for c in a for b in '01')
```

The provided Python script defines a function called `string_xor` that takes two strings `a` and `b` as input. This function performs a binary `XOR` operation on the input strings `a` and `b`, which consist of only 1s and 0s. The binary `XOR` operation returns a string where each character is correct if and only if the corresponding characters in `a` and `b` are different. The `^` operator is used in Python to calculate the binary `XOR` of two digits. Finally, the function joins the resulting characters together with the separator `__` to form the final output string and returns it.