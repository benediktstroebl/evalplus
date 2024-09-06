```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two strings of only ones and zeros
    """
    # xor = [x for x in a] ^ [y for y in b]
    # return ''.join(str(x) for x in xor)
    return "".join(str(x) for x in list(a ^ b))
tests = [
    "010".join("110"),
    "100".join("10"),
    "000".join("10"),
]
for a, b in tests:
    print(f"XOR({a}, {b}): {string_xor(a, b)})
```
The function xor() takes two parameters, a and b, representing two strings that consist only of the characters '0'. It then applies the XOR operation to these two strings and returns the result as a single string.