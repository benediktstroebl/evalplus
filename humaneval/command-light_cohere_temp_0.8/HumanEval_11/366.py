```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two input strings consisting of only ones and zeros.
    a and b are transformed into binary representation, 
    then XOR value is calculated and returned.
    """
    a function takes two strings a and b as input and returns the XOR result as a string.
    """
    test suite:
    assert string_xor('010', '110') == '100'
    assert string_xor('1010', '10110') == '100'
    assert string_xor('000', '1111') == '1110'
    assert string_xor('1111', '000') == '1111'
```
The function `string_xor` takes two strings `a` and `b` as input and returns the XOR of the two strings. The test suite contains passing the the test the function with different inputs and asserting the result is equal to the expected output.