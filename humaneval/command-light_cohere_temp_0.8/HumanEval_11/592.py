```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two strings, a and b, consisting only of single characters.
    Args:
    a: string, same character set as b
    b: string, same character set as a
    Returns: string: a XOR of a and b
    """
    # similar to the above input strings
    return "".join("".join([chr(i) for i in [a, b]))
# test case
print(string_xor("010", "110"))
```