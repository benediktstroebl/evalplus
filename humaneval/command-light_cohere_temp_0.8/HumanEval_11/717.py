```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform XOR operation on two strings and return the result as a string.
    :
    a and b can consist only of the characters '0' and '1'.
    return ''.join('a', b)

# Test suite
def test_string_xor():
    assert string_xor('010', '110') == '100'
    assert string_xor('000', '111') == '11111'
    assert string_xor('111', '110') == '01001'
    assert string_xor('001111', '1110') == '11011000'
    assert string_xor('000111', '1110') == '11011000'
    assert string_xor('1111', '0') == '1'
    assert string_xor('1000', '0000') == '00001000'

# Example usage
test_string_xor()
```
This Python code defines a function `string_xor` that performs an XOR operation on two input strings consisting only of the characters '0' and '1'. The `test_string_xor` function contains a series of assertions that verify the correctness of the `string_xor` function. The code also provides an example usage of the function.