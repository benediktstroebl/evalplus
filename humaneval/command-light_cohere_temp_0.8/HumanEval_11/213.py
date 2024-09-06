```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two input strings.
    >>> string_xor('010', '110')
    '100'
    """
    return a ^ b

def test_string_xor():
    """ Test function for the string_xor function
    """
    assert string_xor('010', '110') == '100'
    assert string_xor('111', '11') == '1111'
    assert string_xor('000', '0000') == '0000'
    assert string_xor('1000', '1111') == '1110000'
    assert string_xor('1010', '1110') == '1001101'
    assert string_xor('0000', '001') == '010000'
```
The code defines a Python function `string_xor` that performs a bitwise XOR operation between two input strings. It uses the with a type hint to ensure the input strings are of type `str`. The test function `test_string_xor` contains several test cases that verify the correctness of the `string_xor` function.