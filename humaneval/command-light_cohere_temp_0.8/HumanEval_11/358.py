```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform XOR operation on two strings composed of only digits 1 and 0 and return the result as a string. """
    a operation is simply: append all 1s to the first number, and 0s to the second number.
    >>> string_xor('010', '110')
    '100'
    """
    return str(append(list("1" * len(a)), a) ^ b)
```