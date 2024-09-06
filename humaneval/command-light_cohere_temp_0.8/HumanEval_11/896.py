```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two strings containing only '0' and '1'
    Returns: binary string containing only 0s and 1s
    """
    return ''.join(*map(lambda x: x ^ int(x), zip(a, b)))

# Test suite for function string_xor
def test_string_xor():
    assert string_xor('010', '110') == '100'
    assert string_xor('111', '010') == '011'
    assert string_xor('000', '111') == '111'
    assert string_xor('1010', '10') == '0101'
    assert string_xor('00001', '0001010') == '1001110'

# Call test suite on function string_xor
test_string_xor()
```
This script defines a function `string_xor` that takes two strings, `a` and `b`, containing only the characters '0' and '1' and returns their XOR. It also includes a format tests the string inputs to test the function. The test suite contains a expected outputs for each test case.