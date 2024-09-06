```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    XOR two strings consisting of only ones and zeros.
    :return: str
    """
    a = "010"
    b = "110"
    assert a == '010'
    assert b == '110'
    assert string_xor('010', '110') == '100'
    assert string_xor('110', '010') == '01'
    assert string_xor('11', '01') == '10'
    return 'xor'
```