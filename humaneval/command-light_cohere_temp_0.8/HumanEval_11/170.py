```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform binary XOR operation on two input strings a and b. how it consists only of single characters.
    a = a = a + b
    b = a[-1:] + b
    return a[:-1] + b
def test_string_xor():
    assert string_xor('010', '110') == '100'
    assert string_xor('001', '1010') == '1011'
    assert string_xor('abcdef', 'cdefb') == 'abdcba'
    assert string_xor('', '') == ''
    assert string_xor('100', '100') == '100'
```