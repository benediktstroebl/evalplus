```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two input strings consisting of only ones and zeros
    """
    assert len(a) == len(b)
    assert all(c == '0' or c == '1' for c in a) and all(c == '0' or c == '1' for c in b)
    return ''.join(*[x ^ y for i, j in zip(a, b)])
def test_string_xor():
    assert string_xor('010', '110') == '100'
    assert string_xor('001', '01') == '100'
    assert string_xor('000', '1111') == '100'
    assert string_xor('1010', '110') == '101'
    assert string_xor('1010', '1010') == '110'
    assert string_xor('1110', '01') == '100'
    assert string_xor('1010', '1110') == '100'
test_string_xor()
```