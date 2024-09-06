```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform binary XOR operation on two strings, and return the result as a string.
    >>> string_xor('010', '110')
    '100'
    >>> string_xor('abc', 'abc')
    'abc'
    >>> string_xor('', '')
    ''
    >>> string_xor('00', '111')
    '11100'
    >>> string_xor('111', '00')
    '00'
    >>> [0] = [1, 0, 1, 1]
    True
    >>> string_xor('aa', 'aa')
    'aa'
    >>> string_xor('', '1')
    '1'
    ```  This code defines a function `string_xor` that performs the XOR operation on two input strings and returns the result as a string. It uses the test XOR operation, which is the logical operation that takes two numbers and returns the result of their XOR.  The result that result of the operation, the first number will be removed from the result.