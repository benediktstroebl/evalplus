```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform XOR operation on two strings consisting of only digits 1 and 0.
    Returns the input and result as strings.
    # Convert input strings to lists of characters
    a = '101010'
    b = '1110'
    result = []
    while a:
        char = int(a[0])
        if char == 1:
            result.append(0)
        elif char == 0:
            result.append(1)
        a = a[1:]
    while b:
        char = int(b[0])
        if char == 1:
            result.append(0)
        elif char == 0:
            result.append(1)
        b = b[1:]
    return ''.join(result)
```