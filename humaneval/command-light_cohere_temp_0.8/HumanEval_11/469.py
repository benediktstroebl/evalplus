```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # convert string to list of characters
    al = list(a)
    bl = list(b)
    # remove all non-ones from lists
    al = [c for c in al if c == '1']
    bl = [c for c in bl if c == '1']
    # perform XOR on the characters
    return ''.join(''.join(al) ^ [bl])
```