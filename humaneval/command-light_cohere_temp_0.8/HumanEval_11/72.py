```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform XOR on two strings consisting of only ones.
    a = a[:]
    b = b[:]
    return ''.join([i ^ j for i in '01' and j in '01' for i, j in zip(a, b)])

#Test the function
def test_string_xor():
    assert string_xor('010', '110') == '100'
    assert string_xor('00', '01') == '11'
    assert string_xor('000', '010') == '110'
    assert string_xor('111', '01') == '1001'
    assert string_xor('0000', '1000') == '1000'
    assert string_xor('111', '111') == '0000'
# Run the test function
test_string_xor()
```