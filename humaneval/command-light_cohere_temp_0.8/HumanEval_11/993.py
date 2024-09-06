```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two strings consisting of only ones and zeros.
    :param 
        a string a: The first string.
    :param 
        string b: The second string
    :return: The XOR of a and b
    """
    return "".join(str(ord(c) ^ ord(b[i]) for i, c in enumerate(a + b)))

# Tests
def test_string_xor():
    assert string_xor('010', '110') == '100'
    assert string_xor('111', '110') == '10'
    assert string_xor('000', '1111') == '1111'
    assert string_xor('1010', '1010') == '0000'
    assert string_xor('00', '10') == '10'
    assert string_xor('0000', '110') == '0000'
```
Do you want help with anything else?