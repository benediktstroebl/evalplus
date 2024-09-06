```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform XOR operation on two strings,
    ensures all input characters are ones.
    """
    algorithm: (a|b) ^ b
    """
    return (''.join(map(lambda x: x ^ ord(x), ''.join(b, a))))
```
This script defines a function `string_xor` that performs the XOR operation on two input strings and returns the result as a string.