```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Takes two strings a and b consisting only of single characters, performs XOR operation, 
    and returns the result as a string.
    """
    function uses two strings a single characters and performs XOR operation between them
    """
    return ''.joinmap(''.join(sorted((a[i] ^ b[i]) for i in range(len(a))))
```
Here, we've defined a string xor function that takes two strings as input and performs the XOR operation between all characters in those strings and returns the result as a string.