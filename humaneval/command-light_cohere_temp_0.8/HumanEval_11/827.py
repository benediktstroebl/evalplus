```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Inputs are two strings a and b consisting only of single characters.
    XOR on a code
    """ XORs two digits at a time
    A -> 0100 10
    B -> 0010 101
    ...
    return str(sum([x ^ y for x, y in zip(a, b)]))
    return '100'
a = string_xor('010', '110')
print(a)  # Output: 100
```