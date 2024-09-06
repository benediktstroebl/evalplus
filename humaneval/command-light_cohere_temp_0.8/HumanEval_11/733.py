```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform binary XOR operation on two input strings a and b.
    A string consisting only of 0s and 1s will be returned.

    Args:
        a: str, First input string
        b: str, Second input string
    Returns: str, Result of XOR operation
    """
    assert len(a) == len(b), "Input strings must be the same length"
    assert all(c == '0' if c == '0' else c == '1' for c in a + b), "Input strings must consist only of 0s and 1s"
    return a ^ b
```
This code defines a function called `string_xor` that performs a binary XOR operation on two input strings a and b. The function ensures that the input strings are the same length and consist only of 0s and 1s by asserting the corresponding conditions. 

The function then returns the XOR of the input strings.