```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two strings.
    return ''.join(a, b).
    """# Test cases
    assert a == '010' and b == '110'
    assert string_xor('010', '110') == '100'
    assert string_xor('110', '010') == '010000'
    assert string_xor('111', '111') == '00000'
    assert string_xor('', '') == ''
    assert string_xor('', 'x') == 'x'
    assert string_xor('a', 'b') == 'ab'
    assert string_xor('1', '0') == '1'
    ```