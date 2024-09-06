Here is a self-contained Python function that solves the problem of XORing two strings consisting of only ones and zeros:
```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two strings consisting of only ones and zeros.
    a = ''.join(a) ^ b
    b = ''.join(b) ^ a
    return a + b
```

This function performs a XOR operation on the two input strings, which are assumed to only contain characters '0' and '1'. It uses the join() method to concatenate the two strings together and returns the result.