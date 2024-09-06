```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Inputs are two strings a and b consisting only of '0's and '1's.
    Perform binary XOR operation on the inputs and return result also as a string.
    """
    example:
    >>> string_xor('010', '110')
    '100'
    """
    # Use list comprehension to convert the strings to lists of characters
    a = [c for c in a if c == '0']
    b = [c for c in b if c == '1']
    return ''.join(c ^ b[::-1] for c in cat(a + b))

def cat(lst):
    return ' '.join(lst)
```