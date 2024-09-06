```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform XOR operation on two strings a and b and return the result as a string.
    :
    test_xor('010', '110')
    assert string_xor('010', '110') == '100'
    assert string_xor('111', '010') == '011'
    assert string_xor('101', '001') == '101'
    assert string_xor('100', '011') == '100'
    assert string_xor('001', '101') == '101'
    assert string_xor('000', '0000') == '0000'
    return 'XORed'  # just for demonstration, actual return can be different
    ```