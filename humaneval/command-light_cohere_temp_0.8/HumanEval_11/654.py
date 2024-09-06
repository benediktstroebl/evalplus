```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two input strings consisting of only '1' and '0'.
    """
    return ''.join(str(a[i] ^ b[i]) for i in range(len(a)))
```
We have created a function named `string_xor` that takes two input strings `a` and `b` and returns the XOR of these strings. 
We use a join function to iterate through each character of the input strings and XOR them together.