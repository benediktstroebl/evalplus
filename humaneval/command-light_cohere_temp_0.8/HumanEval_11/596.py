```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform binary XOR operation on two strings.
    Args:
        - str: a string containing only digits 0 and 1.
    - b: str: another string containing only digits 0 and 1.
    Returns: str: their XOR
    """
    return str(str(str.join('10').join([str[i] & 1 for i in range(len(a)))))
def test_string_xor():
    assert string_xor('010', '110') == '100'
    assert string_xor('001', '11') == '101'
    assert string_xor('1000', '01') == '1001'
    assert string_xor('1010', '10') == '110'
    assert string_xor('0011', '1000') == '1010'
    assert string_xor('001000', '01001') == '10011'
    assert string_xor('101010', '1101010') == '0110110'
```