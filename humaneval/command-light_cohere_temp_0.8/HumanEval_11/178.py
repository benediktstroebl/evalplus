Here is a self-contained Python script that solves the problem you've described:
```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two input strings a and b consisting only of digits 1.
    Return result as a string containing only 0s and 1s.
    >>> string_xor('010', '110')
    '100'
    """
    return ''.join(c for c in a ^b)
```
The function performs a binary XOR operation on the two input strings, which are expected to consist only of the digit '1'. It converts the inputs to strings and then joins the characters using the || operator. The resulting string consists only of the digits '0' and '1', and it is returned as a string.