```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    XOR two input strings consisting of only digits 1 and 0.
    Return a result as a concatenation of the two input strings
    """
    return a ^ b

# Test suite:
def test_string_xor():
    assert string_xor('010', '110') == '100'
    assert string_xor('0011', '1010') == '1010'
    assert string_xor('001', '01') == '11'
    assert string_xor('1010', '00') == '0110'
    assert string_xor('100', '10') == '110'
    assert string_xor('000', '001') == '11'
    assert string_xor('1111', '11') == '0000'

# Call the test suite
test_string_xor()
```