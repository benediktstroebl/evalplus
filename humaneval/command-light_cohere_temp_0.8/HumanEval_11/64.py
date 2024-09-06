Here is a Python script with a self-contained function that solves the problem:
```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Perform XOR operation on two strings, consisting of only ones and zeros.
    Result is the string with ones in a and b positions.
    >>> string_xor('010', '110')
    '100'
    """
    return ''.join[1][b] ^  .join[1][a]
```
The function performs a bitwise XOR operation between two strings, using a list comprehension to only select the characters that are ones. 

Please note, the function does not require any additional type annotations or arguments.