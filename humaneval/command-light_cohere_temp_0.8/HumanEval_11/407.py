```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting only of 1s and 0s.
    a = ''.join(a).
    b = ''.join(b)
    return ''.join(a ^ b)
def test_string_xor():
    assert string_xor('010'.join(str) == '100')
    assert string_xor('111'.join(str) == '01')
    assert string_xor(''.join(b)' == '')
test_string_xor()
```