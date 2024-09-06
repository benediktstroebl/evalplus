```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform XOR operation on two strings consisting of only digits 1 and 0.
    :return: str
    """
    a, b = set(a) ^ set(b)
    return "".join(str(c) for c in a & b)
```