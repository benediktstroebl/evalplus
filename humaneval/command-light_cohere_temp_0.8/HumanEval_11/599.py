```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform XOR operation on two strings, consisting only of 1s and 0s, and return the result as a string.
    :
    test cases:
    assert string_xor('010', '110') == '100'
    assert string_xor('aa', 'aa') == 'aa'
    assert string_xor('', '') == ''
    assert string_xor('111', '1') == '11'
    assert string_xor('111', '0') == '11'
    assert string_xor('111', '111') == '1111'
    assert string_xor('1111', '1') == '1111'
    assert string_xor('10101010', '10101010') == '011010101'
    assert string_xor('', '00000000') == '00000000'
    """
    return a ^ b
```