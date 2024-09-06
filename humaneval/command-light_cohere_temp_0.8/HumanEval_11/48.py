```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting only of ones and zeros.
    a = a + b if len(a)==len(b) else len(a)
    b = b + (b if a else '')
    return a^b
def test_string_xor():
    assert string_xor('010', '110') == '100'
    assert string_xor('110', '010') == '0110'
    assert string_xor('111', '1') == '001'
    assert string_xor('', '') == ''
    assert string_xor('', '1') == '1'
    assert string_xor('a', 'b') == 'ab'
    assert string_xor('abcde', 'fgh') == 'efgh'
    assert string_xor('abcdef', '12345678') == '12345678'
```