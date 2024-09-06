Certainly, here's a self-contained Python script with a function that solves the problem you described:

```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR operation on the inputs and return the result as a string.
    >>> string_xor('010', '110')
    '100'
    """
    return a ^ b
```

This code defines a function named `string_xor` that takes two string inputs (`a` and `b`) and performs the binary XOR operation on them. It then returns the For string result of the operation.