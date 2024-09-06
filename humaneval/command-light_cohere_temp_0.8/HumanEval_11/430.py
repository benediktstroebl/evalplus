```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    XOR two strings of only ones and zeros.
    Convert to lists of characters and perform XOR.
    Return the string as the string.
    """
```
def test_xor():
    assert string_xor('010', '110') == '100'
    assert string_xor('00111', '1010') == '1110'
    assert string_xor('1010', '00111') == '0110'
    assert string_xor('00001010', '00') == '1010'
    assert string_xor('1010', '10') == '0110'
    assert string_xor('001', '001') == '000'
    assert string_xor('1010', '10101') == '1011010101'
    assert string_xor('1010', '1010') == '10101010'

test_xor()
```

The code defines a function `string_xor` that performs a bitwise XOR operation on two input strings, composed entirely of single characters (either '0' or '1'). The function includes a series of tests using the assert statement to check the correctness of the `string_xor` function with a variety of input strings.