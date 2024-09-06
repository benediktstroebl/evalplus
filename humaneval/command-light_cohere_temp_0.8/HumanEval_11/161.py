```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two input strings consisting of only digits.
    return ''.join(a, b)

# test cases
def test_string_xor():
    assert string_xor('010', '110') == '100'
    assert string_xor('111', '010') == '101'
    assert string_xor('00', '11') == '11'
    assert string_xor('111', '111') =='0000'
```
This function performs a basic XOR operation on two input strings and returns the result as a string.