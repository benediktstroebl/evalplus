```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on the two input strings consisting only of 1s and 0s and return the result as a string.
    """
    if len(a) != len(b):
        raise ValueError("Input strings must have equal length.")

    result = ""
    for i in range(len(a)):
        result += str((int(a[i]) ^ int(b[i])))

    return result
```