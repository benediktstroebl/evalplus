```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform XOR operation on two strings, consisting only of ones and 0s.
    Return the string
   
    """ Convert the input strings to lists of characters, then use bitwise XOR operation to build the result.
    >>> char_list_010 = ['0', '1', '0', '0']
    >>> char_list_110 = ['1', '0', '0', '0', '1']
    >>> string_xor('010', '110')
    ['100']
```