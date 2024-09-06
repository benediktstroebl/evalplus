```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    Perform XOR operation on two input strings.
    1s characters only single digit and 0, as the input.
    Perform bitwise XOR operation on the inputs and return the result.
    Return value 'result'.
    """
    if len(a) != len(b):
        raise ValueError("Input strings must have the same length")
    return "".join(x ^ int(b[i]) for i, x in enumerate(a))
```