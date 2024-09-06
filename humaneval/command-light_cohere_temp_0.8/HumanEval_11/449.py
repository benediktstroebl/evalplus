```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform binary XOR on two strings, consisting only of 1s and 0s.
    :return a string resulting from performing XOR operation
    """
    # convert the input to list of digits
    a = ''.join(a)
    b = ''.join(b)
    # remove all non-digit characters
    a = [c for c in a if c in '01']
    b = [c for c in b if c in '01']
    # XOR two lists
    return ''.join(a ^ b)
```