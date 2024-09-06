```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two strings of only ones and zeros.
    return ''.join(a[i] ^ b[i] for i in range(len(a)))
    """
    return ''.join(chr(int(c, 2) ^ int(d, 2)) for c, d in zip(a, b))

# Test cases
def test_string_xor():
    assert string_xor('010', '110') == '100'
    assert string_xor('0011', '1010') == '1010'
    assert string_xor('000', '1111') == '1111'
    assert string_xor('1010', '1111') == '0000'
    assert string_xor('ABC123', 'CDEF456') == 'BCDF456'

# main function call
test_string_xor()
```