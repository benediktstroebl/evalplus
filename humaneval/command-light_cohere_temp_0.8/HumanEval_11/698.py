Here is a Python script that defines a self-contained function `string_xor` solving the problem you described:

```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    : Perform binary XOR on these inputs and return result also as a string.
    :
    result: 010010
    """
    a = '010'
    b = '110'
    return a ^ b
```

The function takes two strings as input and returns the XOR of the two strings. It uses the string `^^` (which is the xor operator) to perform the XOR operation on the two strings.