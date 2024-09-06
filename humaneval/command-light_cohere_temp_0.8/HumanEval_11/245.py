```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform binary XOR operation on two strings a and b consisting only of 1s and 0s and return the result as a string. """
    Input strings a string_xor('010', '110')
    '100'
    """
    a = List(filter(str.isdigit, a)) + List(filter(str.isdigit, b))
    b = a[:-len(a)] + a[-len(a):]
    return ''.join(b)
```